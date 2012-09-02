#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
routing decorator

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

import seshat.baseURL as bu


def route(routeURL):
        def wrapper(HTTPObject):
                global urls
                urlObject = bu.url(routeURL, HTTPObject)
                urls.append(urlObject)
                HTTPObject.__url__ = routeURL
                return HTTPObject
        return wrapper
