from flask import Flask, render_template, request
from flask import jsonify
import json
import pymysql.cursors
from datetime import datetime, date
import decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = "dfdfdffdad"

# connect with database
conn = pymysql.connect(host='localhost',
                       user='root',
                       db='dbp',
                       cursorclass=pymysql.cursors.DictCursor)

cursor = conn.cursor()


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        else:
            return json.JSONEncoder.default(self, obj)
# 使用


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


@app.route('/search_flight', methods=['POST'])
# def search():
#     data = request.form['search']
#     table = ['yxx', 'yaoming', 'edward']
#     if data in table:
#         d = {'result': True}
#     else:
#         d = {'result': False}
#     return jsonify(d)
def search_flight():
    result = ''
    try:
        source = request.form['source_ca']
        arrival = request.form['arrival_ca']
        date = request.form['departure_date']

        # need to support city

        sql = "SELECT * FROM flight WHERE departure_airport = \'" + str(source) + "\' and arrival_airport = \'" + str(arrival) + "\'"
        cursor.execute(sql)
        result = cursor.fetchall()  # fetchmany: return a certain number of results
        conn.commit()
    finally:
        result_final = ''
        for item in result:
            result_final += json.dumps(item, indent=2, cls=CJsonEncoder, ensure_ascii=False)[3:-2] + "[]"
        return result_final


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
    table = [('id', 'name', 'age', 'score'),
        ('1', 'xiemanrui', '18', '100'),
        ('2', 'yxx', '18', '100'),
        ('3', 'yaoming', '37', '88')]

    print('mytable')
    data = json.dumps(table)
    print(data)
    return data


@app.route('/insert_airline', methods=['POST'])
def insert_airline():
    result = ''
    try:
        data = request.form['insert_airline']
        sql = "INSERT INTO airline VALUES " + "(\'" + data + "\')"
        cursor.execute(sql)
        conn.commit()
    finally:
        return "success"


if __name__ == '__main__':
    app.run()


