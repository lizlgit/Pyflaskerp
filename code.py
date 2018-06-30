#!/usr/bin/env python3
# -*- coding=utf8 -*-
# 导入Flask库
from flask import Flask
from flask import request
from flask import render_template
from sql import fordata,logindata
app = Flask(__name__)

# 启动服务器后运行的第一个函数，显示对应的网页内容
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('login.html')

# 对登录的用户名和密码进行判断
@app.route('/login', methods=['POST'])
def login():
    un = str(request.form['username'])
    pw = str(request.form['password'])
    re = logindata(un,pw)
    if re == True:
        return render_template('index.html')
    else :
        return 'ERROR!!!'

# 显示教师首页的函数，可以显示首页里的信息
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

# 显示教学计划的函数，当有请求发生时，去数据库里查找对应的数据，
# 然后将数据的格式用for循环进行遍历，变成列表的格式，然后返回到页面中，
# 再由页面进行显示数据
@app.route('/select', methods=['GET'])
def select():
    # 调用数据库函数，获取数据
    data = fordata('user',1)
    # 用列表的格式存放全部数据
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        dict_data['e'] = value[4]
        dict_data['f'] = value[5]
        posts.append(dict_data)
    # print posts
    return render_template('list.html', posts=posts)


# 显示管理班的函数页面
@app.route('/indata', methods=['GET'])
def indata():
    # 调用数据库函数，获取数据
    data = fordata('jihuaxijie',2)
    # 用列表的格式存放全部数据
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        dict_data['e'] = value[4]
        dict_data['f'] = value[5]
        posts.append(dict_data)
    # print posts
    return render_template('list.html', posts=posts)

# 显示排课信息的函数页面
@app.route('/outdata', methods=['GET'])
def outdata():
    # 调用数据库函数，获取数据
    data = fordata('jihuaxijie',3)
    # 用列表的格式存放全部数据
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        dict_data['e'] = value[4]
        dict_data['f'] = value[5]
        posts.append(dict_data)
    # print posts
    return render_template('list.html', posts=posts)

# 显示学生成绩的页面，包括调用学生成绩数据表
@app.route('/manage', methods=['GET'])
def manage():
    # 调用数据库函数，获取数据
    data = fordata('jihuaxijie',4)
    # 用列表的格式存放全部数据
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        dict_data['e'] = value[4]
        dict_data['f'] = value[5]
        posts.append(dict_data)
    # print posts
    return render_template('list.html', posts=posts)

# 主函数
if __name__ == '__main__':
    #app.debug = True
    app.run()
