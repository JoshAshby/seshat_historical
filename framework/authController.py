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
from route import route
import authModel as am
import authView as av
from authWrap import auth


@route(subURL["auth"] + "/login")
class login(basePage):
        def GET(self):
                """
                Display the login page.
                """
                if self.session.has_key("login") and self.session["login"] is True:
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", baseURL + "/")]
                else:
                        view = av.loginView("HTML")

                        return view.build()

        def POST(self):
                """
                Use form data to check login, and the redirect if successful
                if not redirect to login page again.
                """
                passwd = self.members["passwd"]
                name = self.members["user"]

                self.session = am.loginUser(name, passwd, self.session)

                if self.session.has_key('login') and self.session['login'] is True:
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", baseURL + "/")]
                else:
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", baseURL + subURL["auth"] + "/login")]


@route(subURL["auth"] + "/logout")
class logout(basePage):
        def GET(self):
                """
                Simply log the user out. Nothing much to do here.

                redirect to login page after we're done.
                """
                self.session = am.logoutUser(self.session)

                self.status = "303 SEE OTHER"
                self.headers = [("location", (subURLLink["auth"] + "/login"))]


@route(subURL["auth"] + "/new/user")
class newUser(basePage):
        @auth
        def GET(self):
                """
                This will eventually give a nice form in order to
                make a new user, right now it does nothing however.
                """
                pass

        @auth
        def PUT(self):
                """

                """
                pass
