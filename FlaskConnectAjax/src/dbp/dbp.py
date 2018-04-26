from flask import Flask, render_template, request
from flask import jsonify
import json
import pymysql.cursors


app = Flask(__name__)

# configure MySQL
conn = pymysql.connect(host='localhost',
                       user='root',
                       db='dbp',
                       cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mystring')
def mystring():
    return 'my string'


@app.route('/dataFromAjax')
def dataFromAjax():
    test = request.args.get('mydata')
    print(test)
    return 'dataFromAjax'


@app.route('/mydict', methods=['GET', 'POST'])
def mydict():
    print('post')
    if request.method == 'POST':
        a = request.form['mydata']
        print(a)
    d = {'name': 'xmr', 'age': 18}
    return jsonify(d)


@app.route('/name', methods=['POST'])
def getname():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    d = {'name': firstname + ' ' + lastname, 'age': 18}
    print(d)
    return jsonify(d)


@app.route('/myform', methods=['POST'])
def myform():
    print('post')
    a = request.form['FirstName']
    print(a)
    d = {'name': 'xmr', 'age': 18}
    return jsonify(d)


@app.route('/mylist')
def mylist():
    l = ['xmr', 18]
    print('mylist')
    return json.dumps(l)  # 用jsonify前端会出错


@app.route('/mytable')
def mytable():
    table = []
    cursor = conn.cursor()
    query = 'select * from `airport`'
    cursor.execute(query)
    raw_data = cursor.fetchall()
    if raw_data:
        title = tuple(raw_data[0].keys())
        table.append(title)
        for item in raw_data:
            table.append(tuple(item.values()))
        data = json.dumps(table)
        return data
    else:
        return 0


if __name__ == '__main__':
    app.run()
