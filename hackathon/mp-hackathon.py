from flask import Flask, request, jsonify, redirect

from hackathon.mysql_util import within_conn


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/register', methods=['POST'])
def enter_user():
    name = request.form['name']
    redirect_to_index = redirect('/index')
    response = app.make_response(redirect_to_index)
    response.set_cookie('mp-hackaton-user', value=name)
    return response


@app.route('/item')
def items():
    def db_action(cnx, cursor):
        cursor.execute("SELECT * FROM item")
        return cursor.fetchall()

    items = within_conn(lambda cnx, cursor: db_action(cnx, cursor))
    items_json = map(lambda (id, title, photo, description): {"title": title, "photo": photo}, items)
    return jsonify(items=items_json)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
