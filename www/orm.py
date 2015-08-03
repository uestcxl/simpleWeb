#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio, logging

import aiomysql

__author__ = 'xl'


def log(sql, args=()):
	logging.info('SQL: %s' % sql)
	pass

#创建连接池，复用数据库连接
@asyncio.coroutine
def create_pool(loop, **kw):
	logging.info('host', 'localhost')
	global __pool
	__pool = yield from aiomysql.create_pool(
		host = kw.get('host', 'localhost'),
		port = kw.get('port', 3306),
		user = kw['user'],
		password = kw['password'],
		db = kw['db'],
		charset = kw.get('charset', 'utf8'),
		autocommit = kw.get('autocommit', True),
		maxsize = kw.get('maxsize', 10),
		minsize = kw.get('minsize', 1),
		loop = loop
		)

@asyncio.coroutine
def select(sql, args, size=None):
	log(sql, args)
	