#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
controller for authentication stuff.

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

import framework as fw
from baseObject import baseHTTPPageObject as basePage
from route import *
import authModel as am
import authView as av
from authWrap import *


@route(subURL["auth"] + "/login")
class login(basePage):
        def GET(self):
                """
                Display the login page
                """
                view = av.loginView()

                return view.build()

        def POST(self):
                """
                log the user in
                """
                passwd = self.members["passwd"]
                name = self.members["user"]

                self.session = am.loginUser(name, passwd, self.session)

                self.status = "303 SEE OTHER"
                self.headers = [("location", baseURL + "/")]


@route(subURL["auth"] + "/logout")
class logout(basePage):
        def GET(self):
                """

                """
                self.session = am.logoutUser(self.session)

                self.status = "303 SEE OTHER"
                self.headers = [("location", (subURLLink["auth"] + "/login"))]


@route(subURL["auth"] + "/new/user")
class newUser(basePage):
        @auth
        def GET(self):
                """

                """
                pass

        @auth
        def PUT(self):
                """

                """
                pass
