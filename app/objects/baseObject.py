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
        import config as c
except:
        abspath = os.path.dirname(__file__)
        sys.path.append(abspath)
        os.chdir(abspath)
        import config as c

import models.sessionModel as sm

class baseHTTPPageObject(object):
        __level__ = None
        """
        Base HTTP page response object
        This determins which REQUEST method to send to,
        along with authentication level needed to access the object.
        """
        def __init__(self, env, members):
                self.env = env
                self.members = members
                self.method = env["REQUEST_METHOD"]

                self.head = ("200 OK", 
                        [
                                ("Content-type", "text/html"),
                        ])

        def build(self, data, reply):
                error = False

#                if c.session.history:
#                        self.head = ("303 SEE OTHER", [("location", c.session.history)])
#                        c.session.history = ""
#                        error = True

                content = ""

                matches = c.authRegex.findall(str(self.__class__.__name__))
                if not error and self.__level__:
                        if c.session.user["level"] == "GOD":
                                """
                                Duh, This user is obviously omnicious and has access to every
                                area in the site.
                                """
                                pass

                        else:
                                if self.__level__ != c.session.user.level:
                                        c.session.pushMessage("You need to have %s rights to access this." % self.__level__, "error")
                                        self.head = ("303 SEE OTHER", [("location", "/auth/login")])
                                        c.session.history = self.__url__
                                        error = True

                                else:
                                        pass

                if not error:
                        content = getattr(self, self.method)() or ""

                data.put(content)
                data.put(StopIteration)

                reply.put(self.head)
                reply.put(StopIteration)

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
