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

import seshat.framework as fw
from baseObject import baseHTTPPageObject as basePage
from seshat.route import route

import re

import views.baseView as bv


@route(subURL["auth"] + "/login")
class login(basePage):
        def GET(self):
                """
                Display the login page.
                """
                if self.session["username"]:
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", baseURL + "/")]
                        self.session.pushMessage("Hey look, you're already signed in!")
                        return ""
                else:
                        view = bv.noSidebarView()
                        loginForm = bf.baseForm()

                        loginForm = loginForm.build()

                        view["content"] = loginForm

                        return view.build()

        def POST(self):
                """
                Use form data to check login, and the redirect if successful
                if not redirect to login page again.
                """
                passwd = self.members["password"]
                name = self.members["username"]

                try:
                        self.session.login(name, passwd)
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", baseURL + "/")]
                except:
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", subURL["auth"] + "/login")]
                        self.session.pushMessage("Something went wrong with your username or password, plase try again.", "error")

                return ""


@route(subURL["auth"] + "/logout")
class logout(basePage):
        def GET(self):
                """
                Simply log the user out. Nothing much to do here.

                redirect to login page after we're done.
                """
                self.session.logout()

                self.status = "303 SEE OTHER"
                self.headers = [("location", (subURL["auth"] + "/login"))]

                return ""
