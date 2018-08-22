#!/usr/bin/env python3
# -*- coding=utf8 -*-
from flask import Flask
from flask import render_template,jsonify,request
from sqlmath import add_user,add_supplier

app = Flask(__name__)
#路由定义
@app.route('/')
def login():
    return render_template('index.html')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/data')
def data():
    return render_template('data.html')
@app.route('/add')
def add():
    return render_template('add.html')
@app.route('/gdm')
def gdm():
    return render_template('gdm.html')
@app.route('/edit')
def edit():
    return render_template('edit.html')
@app.route('/find')
def find():
    return render_template('find.html')
@app.route('/count')
def count():
    return render_template('count.html')
@app.route('/manager')
def manager():
    return render_template('manager.html')
#页面请求接收
@app.route('/adduser', methods=['POST'])
def adduser():
    if request.method == 'POST':
        user = request.form.get('user')
        code = request.form.get('code')
        password = request.form.get('password')
        telephone = request.form.get('telephone')
        sts = request.form.get('sts')
        do = add_user(user,code,password,telephone,sts)
        return render_template('manager.html')
    else:
        return 'error'
@app.route('/add_supplier', methods=['POST'])
def add_supp():
    if request.method == 'POST':
        supplier = request.form.get('supplier')
        short_name = request.form.get('short_name')
        linkman = request.form.get('linkman')
        telephone = request.form.get('telephone')
        address = request.form.get('address')
        other = request.form.get('other')
        sts = request.form.get('sts')
        do = add_supplier(supplier,short_name,linkman,telephone,address,other,sts)
        return render_template('gdm.html')
    else:
        return 'error'
#表格数据接口 未完成
@app.route('/api/userlist', methods=['GET','POST'])
def userlist():
    return jsonify(re)

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=8000)
