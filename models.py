#! /usr/bin/env python3
# -*- coding=utf8 -*-
from setting import db

class User(db.Model):
    user = db.Column(db.String(255))
    code = db.Column(db.String(255),primary_key=True)
    password = db.Column(db.String(255))
    telephone = db.Column(db.String(255))
    create_time = db.Column(db.DateTime)
    sts = db.Column(db.Integer)

    def __init__(self,user,code,password,telephone,create_time,sts):
        self.user = user
        self.code = code
        self.password = password
        self.telephone = telephone
        self.create_time = create_time
        self.sts = sts
    def __repr__(self):
        return '<User %r>' % self.user

class Goods(db.Model):
    id = db.Column('型号编号',db.Integer,primary_key=True)
    goods_id = db.Column(db.String(255))
    SN = db.Column(db.String(255))
    model_id = db.Column(db.String(255))
    in_time = db.Column(db.DateTime)
    out_time = db.Column(db.DateTime)
    price_get = db.Column(db.String(255))
    price_sall = db.Column(db.String(255))
    status = db.Column(db.String(255))
    sts = db.Column(db.String(255))

    def __init__(self,id,goods_id,SN,model_id,in_time,out_time,price_get,price_sall,status,sts):
        self.id = id
        self.goods_id = goods_id
        self.SN = SN
        self.model_id = model_id
        self.in_time = in_time
        self.out_time = out_time
        self.price_get = price_get
        self.price_sall = price_sall
        self.status = status
        self.sts = sts

    def __repr__(self):
        return '<Goods %r>' % self.id

class Good_model(db.Model):
    model_id = db.Column(db.String(255),primary_key=True)
    model_name = db.Column(db.String(255))
    model_number = db.Column(db.String(255))
    nuture = db.Column(db.String(255))
    other = db.Column(db.String(255))
    gs_code = db.Column(db.Integer)
    sts = db.Column(db.String(255))

    def __init__(self,model_id,model_name,model_number,nuture,other,gs_code,sts):
        self.model_id = model_id
        self.model_name = model_name
        self.model_number = model_number
        self.nuture = nuture
        self.other = other
        self.gs_code = gs_code
        self.sts = sts
    def __repr__(self):
        return '<User %r>' % self.model_name

class Good_supplier(db.Model):
    gs_code = db.Column(db.Integer,primary_key=True)
    supplier = db.Column(db.String(255))
    short_name = db.Column(db.String(255))
    linkman = db.Column(db.String(255))
    telephone = db.Column(db.String(255))
    address = db.Column(db.String(255))
    other = db.Column(db.String(255))
    sts = db.Column(db.String(255))

    def __init__(self,supplier,short_name,linkman,telephone,address,other,sts):
        self.supplier = supplier
        self.short_name = short_name
        self.linkman = linkman
        self.telephone = telephone
        self.address = address
        self.other = other
        self.sts = sts

    def __repr__(self):
        return '<Goods %r>' % self.supplier

class Good_log(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    goods_id = db.Column(db.String(255))
    create_time = db.Column(db.DateTime)
    status = db.Column(db.String(255))
    sts = db.Column(db.String(255))
    tag = db.Column(db.String(255))
    man_register = db.Column(db.String(255))

    def __init__(self,goods_id,create_time,status,sts,tag,man_register):
        self.goods_id = goods_id
        self.create_time = create_time
        self.status = status
        self.sts = sts
        self.tag = tag
        self.man_register = man_register

    def __repr__(self):
        return '<Goods %r>' % self.supplier
