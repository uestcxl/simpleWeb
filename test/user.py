import sys
sys.path.append("..")

import www.orm
from www.model import User, Blog, Comment

def test():
    yield from orm.create_pool(user='xl', password='xulei123', database='awesome')
    u = user(name='test', email='test@baidu.com', passwd='test', image='about:blank')
    yield from u.save()

for x in test():
    pass
