#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
decorator for use on GET POST PUT DELETE functions
that will check if a user is logged in.

For more information, see: https://github.com/JoshAshby/

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
from authConfig import *


"""
It's important to note that @auth'ed pages can not be generators
and must use return instead of yield
"""
def auth(fn):
        def wrapper(obj):
                if obj.session.has_key('login') and obj.session['login'] is True:
                        return fn(obj)
                else:
                        obj.status = "303 SEE OTHER"
                        obj.headers = [('location', authURL)]
                        return None
        return wrapper
