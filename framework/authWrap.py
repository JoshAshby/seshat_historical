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
import sys, os

try:
        from config import *
except:
        abspath = os.path.dirname(__file__)
        sys.path.append(abspath)
        os.chdir(abspath)
        from config import *


"""
It's important to note that @auth'ed pages can not be generators
and must use return instead of yield
"""
def auth(fn):
        def wrappered(obj):
                if obj.session.has_key('login') and obj.session['login'] is True:
                        return fn(obj)
                else:
                        obj.status = "303 SEE OTHER"
                        obj.headers = [("location", subURLLink["auth"] + "/login")]
        return wrappered
