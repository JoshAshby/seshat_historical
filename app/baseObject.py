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

import re
import gevent


class baseHTTPPageObject(object):
        """

        """
        def __init__(self, env, members):
                self.env = env
                self.session = env["beaker.session"]
                self.members = members
                self.method = env["REQUEST_METHOD"]

                self.status = "200 OK"
                self.headers = [
                        ("Content-type", "text/html"),
                        ]

        def build(self, data):
                authRe = re.compile(authRegex)
                matches = authRe.match(str(self.__class__.__name__))
                matches = matches.groups()

                if matches[0] == "auth":
                        if not session.has_key("login") or not session["login"]:
                                self.status = "303 SEE OTHER"
                                self.headers = [("location", baseURL + subURL["auth"] + "/login")]
                                content = ""
                        else:
                                content = getattr(self, self.method)()
                else:
                        content = getattr(self, self.method)()

                data.put(content)
                data.put(StopIteration)

        def buildHeaders(self, headers):
                headers.put(self.headers)
                headers.put(StopIteration)

        def buildStatus(self, status):
                status.put(self.status)
                status.put(StopIteration)

        def buildCookieJar(self, session):
                session.put(self.session)
                session.put(StopIteration)

        def HEAD(self):
                return self.GET()

        def GET(self):
                pass

        def POST(self):
                pass

        def PUT(self):
                pass

        def DELETE(self):
                pass
