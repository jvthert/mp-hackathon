from flask import Flask, request, jsonify, redirect
from hackathon.mysql_util import within_conn

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

def items_count():
    def db_action(cnx, cursor):
        cursor.execute("SELECT count(*) FROM item")
        return cursor.fetchone()

    return int(within_conn(lambda cnx, cursor: db_action(cnx, cursor))[0])

def load_item(pos):
    def db_action(cnx, cursor):
        query = "SELECT * FROM item LIMIT %s, %s" % (pos, pos + 1)
        cursor.execute(query)
        return cursor.fetchone()

    return within_conn(lambda cnx, cursor: db_action(cnx, cursor))


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/enter_with_get', methods=['GET'])
def enter_user_with_get():
    name = request.args['name']
    return register(name)

@app.route('/register', methods=['POST'])
def enter_user():
    name = request.form['name']
    return register(name)

def register(name):
    def db_action(cnx, cursor):
        insert_query = "INSERT INTO user VALUES (NULL, '%s')" % name
        cursor.execute(insert_query)
    within_conn(lambda cnx, cursor: db_action(cnx, cursor))

    redirect_to_index = redirect('/item')
    response = app.make_response(redirect_to_index )
    response.set_cookie('mp-hackaton-user',value=name)
    return response


@app.route('/item')
def item():
    pos = int(request.cookies.get('mp-hackaton-pos', 0))
    size = items_count()
    pos %= size
    current_item = load_item(pos)
    out = jsonify({"title": current_item[1], "photo": current_item[2], "description": current_item[3]})
    out.set_cookie('mp-hackaton-pos', str(pos + 1))
    return out

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run()

