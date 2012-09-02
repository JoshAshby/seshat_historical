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
import views.forms.baseForm as bf
import views.elements.baseElements as be


@route("/auth/login")
class login(basePage):
        def GET(self):
                """
                Display the login page.
                """
                if self.session.username:
                        self.header = ("303 SEE OTHER", [("location", baseURL + "/")])
                        self.session.pm("Hey look, you're already signed in!")

                else:
                        view = bv.noSidebarView()

                        elements = be.adminElements()
                        view["nav"] = elements.navbar()

                        view["title"] = "Login"
                        view["messages"] = bv.baseRow(self.session.getMessage())

                        loginForm = bf.baseForm(fields=[{
                                "name": "username",
                                "placeholder": "Username",
                                }, {
                                "type": "password",
                                "name": "password",
                                "placeholder": "Password",
                                }, {
                                "type": "submit",
                                "name": "submit",
                                "value": "Login"
                                }], action=("/auth/login"), width=4)

                        view["content"] = bv.baseRow(loginForm, 4, 4)

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
                        self.header = ("303 SEE OTHER", [("location", "/")])
                except e:
                        print e
                        self.header = ("303 SEE OTHER", [("location", "/auth/login")])
                        self.session.pm("Something went wrong with your username or password, plase try again.", "error")


@route("/auth/logout")
class logout(basePage):
        def GET(self):
                """
                Simply log the user out. Nothing much to do here.

                redirect to login page after we're done.
                """
                self.session.logout()

                self.header = ("303 SEE OTHER", [("location", ("/auth/login"))])
