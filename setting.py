#!/usr/bin/env python3
# -*- coding=utf8 -*-
#设定
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#定义数据库连接
def db_init():
    db.create_all()



from models import User
from models import Goods
from models import Good_model
from models import Good_supplier
from models import Good_log
