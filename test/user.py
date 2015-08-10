#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sys, asyncio
sys.path.append("..")

import www.orm
from www.model import User, Blog, Comment

def test(loop):
    yield from www.orm.create_pool(loop=loop, user='xl', password='xulei123', db='awesome')
    u = User(name='test', email='test@baidu.com', passwd='test', image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()