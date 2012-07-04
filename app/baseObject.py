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
import models.authModel as am
import models.sessionModel as sm

class baseHTTPPageObject(object):
        """

        """
        def __init__(self, env, members, sessionId):
                self.env = env
                self.members = members
                self.session = sm.Session(sessionId)
                self.method = env["REQUEST_METHOD"]

                self.status = "200 OK"
                self.headers = [
                        ("Content-type", "text/html"),
                        ]

        def build(self, data, headers, status):
                content = ""
                authRe = re.compile("([^_\W]*)")
                matches = authRe.findall(str(self.__class__.__name__))
                if matches and "auth" in matches:
                        if self.session["level"] == "GOD":
                                content = getattr(self, self.method)()
                        else:
                                if self.session["level"] != "basic":
                                        self.status = "303 SEE OTHER"
                                        self.headers = [("location", baseURL + subURL["auth"] + "/login")]
                                        self.session.pushMessage("You need to be logged in to access this.", "error")
                                if "admin" in matches:
                                        if self.session["level"] != "admin":
                                                self.session.pushMessage("You need to have admin rights to access this.", "error")
                else:
                        content = getattr(self, self.method)()


                data.put(content)
                data.put(StopIteration)

                headers.put(self.headers)
                headers.put(StopIteration)

                status.put(self.status)
                status.put(StopIteration)

                self.session.commit()

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
