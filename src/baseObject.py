#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
baseObject to build pages off of

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


class baseHTTPPageObject(object):
        """

        """
        def __init__(self, env, members):
                self.env = env
                self.session = env["beaker.session"]
                self.members = members

                self.status = "200 OK"
                self.headers = [
                        ("Content-type", "text/html"),
                        ]

        def route(self, method, data):
                self.content = data
                getattr(self, method)()
                data = self.content
                data.put(StopIteration)

        def head(self, headers):
                headers.put(self.headers)
                headers.put(StopIteration)

        def statuss(self, status):
                status.put(self.status)
                status.put(StopIteration)

        def returnCookieJar(self, session):
                session.put(self.session)
                session.put(StopIteration)

        def GET(self):
                pass

        def POST(self):
                pass

        def PUT(self):
                pass

        def DELETE(self):
                pass
