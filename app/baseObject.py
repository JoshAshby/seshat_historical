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
from gevent import queue


class baseHTTPPageObject(object):
        """

        """
        def __init__(self, env, members):
                self.env = env
                self.session = env["beaker.session"]
                self.members = members
                self.method = env["REQUEST_METHOD"]
                self.messages = ""

                self.status = "200 OK"
                self.headers = [
                        ("Content-type", "text/html"),
                        ]

        def build(self, data):
                content = ""
                authRe = re.compile("([^_\W]*)")
                matches = authRe.match(str(self.__class__.__name__))
                if matches:
                        matches = matches.groups()

                        if matches[0] == "auth":
                                if not self.session.has_key("login") or not self.session["login"]:
                                        self.status = "303 SEE OTHER"
                                        self.headers = [("location", baseURL + subURL["auth"] + "/login")]
                                        content = ""

                if not content:
                        content = getattr(self, self.method)()
                if not content:
                        content = ""

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

        def passError(self, message):
                errorMess = """
                <div class="alert alert-error alert-block">
                        <i class="icon-fire"></i> <strong>OH SNAP!!</strong> Looks like something went wrong!<br>
                        %s
                </div>
                """ % message
                self.messages += errorMess

        def passMessage(self, message):
                mess = """
                <div class="alert alert-block">
                        <i class="icon-exclamation-sign"></i> <strong>Don't Worry!!</strong> This isn't bad, just some info for you.<br>
                        %s
                </div>
                """ % message
                self.messages += mess

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
