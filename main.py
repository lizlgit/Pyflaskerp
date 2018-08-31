#!/usr/bin/env python3
# -*- coding=utf8 -*-
from flask import Flask
from flask import render_template,jsonify,request
from sqlmath import add_user,add_supplier,mima
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'whoisyourdad232311132'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # 定义登录的 视图
login_manager.login_message = '请登录以访问此页面'  # 定义需要登录访问页面的提示消息
# 使用user_loader装饰器的回调函数非常重要，他将决定 user 对象是否在登录状态
@login_manager.user_loader
def load_user(code):
    from models import User
    return User.get(code)

@app.route('/loginform', methods=['POST'])
def loginform():
    if request.method == 'POST':
        usercode = request.form.get('usercode')
        password = request.form.get('password')
        do = mima(usercode,password)
        if do == usercode:
            return render_template('index.html')
        else:
            return render_template('login.html')
    else:
        return 'error'
@app.route('/logout')
@login_required
def logout():
    logout_user()  # 登出用户
    return '已经退出登录'
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
#路由定义
@app.route('/')
def login():
    return render_template('login.html')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')
@app.route('/data')
@login_required
def data():
    return render_template('data.html')
@app.route('/mk1')
@login_required
def mk1():
    return render_template('mk1.html')
@app.route('/mk2')
@login_required
def mk2():
    return render_template('mk2.html')
@app.route('/mk3')
@login_required
def mk3():
    return render_template('mk3.html')
@app.route('/find')
@login_required
def find():
    return render_template('find.html')
@app.route('/count')
@login_required
def count():
    return render_template('count.html')
@app.route('/manager')
@login_required
def manager():
    return render_template('manager.html')
#各种页面表单
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
