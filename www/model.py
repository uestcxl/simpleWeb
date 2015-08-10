#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Xu Lei'

import time, uuid
from orm import Model, StringField, IntegerField, BooleanField, TextField, FloatField


#返回唯一的id
def next_int():
    return '%015d%s' % (int(time.time( * 1000)), uuid.uuid4().hex)

class User(Model):
    __table__ = 'user'

    id = StringField(primary_key=True, default=next_int, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(100)')
    create_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_int, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(50)')
    content = TextField()
    create_at = FloatField(time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_int, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(100)')
    content = TextField()
    create_at = FloatField(time.time)
