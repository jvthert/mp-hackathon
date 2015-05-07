from flask import Flask
from flask import jsonify
from mysql_util import within_conn

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/item')
def items():
    def db_action(cnx, cursor):
            cursor.execute("SELECT * FROM item")
            return cursor.fetchall()

    items = within_conn(lambda cnx, cursor: db_action(cnx, cursor))
    items_json = map(lambda (id, title, photo, description): {"title": title, "photo": photo}, items)
    return jsonify(items=items_json)


if __name__ == '__main__':
    app.run()
