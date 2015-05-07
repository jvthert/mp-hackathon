from flask import Flask, request, jsonify
from hackathon.mysql_util import within_conn

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

USER_ID_COOKIE = 'mp-hackathon-userid'
USER_NAME_COOKIE = 'mp-hackathon-username'
POS_COOKIE = 'mp-hackathon-pos'

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(path)

@app.route('/api/enter_with_get', methods=['GET'])
def enter_user_with_get():
    name = request.args['name']
    return register(name)

@app.route('/api/register', methods=['POST'])
def enter_user():
    name = request.values['name']
    return register(name)

def register(name):
    def db_action(cnx, cursor):
        insert_query = "INSERT INTO user VALUES (NULL, '%s')" % name
        cursor.execute(insert_query)
        return cursor.lastrowid
    user_id = within_conn(lambda cnx, cursor: db_action(cnx, cursor))

    response = app.make_response("")
    response.set_cookie(USER_ID_COOKIE, value=str(user_id))
    response.set_cookie(USER_NAME_COOKIE, value=name)
    return response


@app.route('/api/item')
def item():
    pos = int(request.cookies.get(POS_COOKIE, 0))
    size = items_count()
    if pos >= size:
        return "No more items", 404
    current_item = load_item(pos)
    item_json = {
        "id": current_item[0],
        "title": current_item[1],
        "photo": current_item[2],
        "description": current_item[3]
    }
    out = jsonify(item_json)
    out.set_cookie(POS_COOKIE, str(pos + 1))
    return out

@app.route("/api/answer", methods=['POST'])
def appriase():
    user_id = request.cookies.get(USER_ID_COOKIE)
    item_id = request.values['id']
    price = request.values['price']

    def db_action(cnx, cursor):
        insert_query = "INSERT INTO appraisal VALUES(%s, %s, %s)" % (item_id, user_id, price)
        cursor.execute(insert_query)

    within_conn(lambda cnx, cursor: db_action(cnx, cursor))
    return ""


@app.route("/api/results/<int:user_id>", methods=['GET'])
def results(user_id):
    def db_action(cnx, cursor):
        results_query = "SELECT i.title, " \
                       "i.photo, " \
                       "app.price, " \
                       "(select ROUND(avg(price)) from appraisal where item_id = i.id group by item_id) as av, " \
                       "(select count(*) from appraisal where item_id = i.id) total from appraisal app join item i on app.item_id = i.id " \
                       "where app.user_id = %s" % user_id
        cursor.execute(results_query)
        return cursor.fetchall()

    result_list = within_conn(lambda cnx, cursor: db_action(cnx, cursor))

    def to_json(result):
        return {
            "title": result[0],
            "photo": result[1],
            "guess": int(result[2]),
            "avg": int(result[3]),
            "numResults": int(result[4])
        }

    json = map(lambda r: to_json(r), result_list)
    return jsonify(items=json)

def items_count():
    def db_action(cnx, cursor):
        cursor.execute("SELECT COUNT(*) FROM item")
        return cursor.fetchone()

    return int(within_conn(lambda cnx, cursor: db_action(cnx, cursor))[0])

def load_item(pos):
    def db_action(cnx, cursor):
        query = "SELECT * FROM item LIMIT %s, %s" % (pos, 1)
        cursor.execute(query)
        return cursor.fetchone()

    return within_conn(lambda cnx, cursor: db_action(cnx, cursor))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run(threaded=True)

