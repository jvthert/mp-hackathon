import os
from flask import Flask, request, jsonify
from hackathon.mysql_util import within_conn

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

USER_ID_COOKIE = 'mp-hackathon-userid'
USER_NAME_COOKIE = 'mp-hackathon-username'
POS_COOKIE = 'mp-hackathon-pos'


URL_PREFIX = os.getenv("URL_PREFIX", "/api")

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('%s/<path:path>' % URL_PREFIX)
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(path)

@app.route('%s/enter_with_get' % URL_PREFIX, methods=['GET'])
def enter_user_with_get():
    name = request.args['name']
    return register(name)

@app.route('%s/register' % URL_PREFIX, methods=['POST'])
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


@app.route('%s/item' % URL_PREFIX)
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

@app.route("%s/answer" % URL_PREFIX, methods=['POST'])
def appriase():
    user_id = request.cookies.get(USER_ID_COOKIE)
    item_id = request.values['id']
    price = request.values['price']

    def db_action(cnx, cursor):
        insert_query = "INSERT INTO appraisal VALUES(%s, %s, %s)" % (item_id, user_id, price)
        cursor.execute(insert_query)

    within_conn(lambda cnx, cursor: db_action(cnx, cursor))
    return ""

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

