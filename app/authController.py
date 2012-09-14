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
        import config as c
except:
        abspath = os.path.dirname(__file__)
        sys.path.append(abspath)
        os.chdir(abspath)
        import config as c

from objects.baseObject import baseHTTPPageObject as basePage
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
                if c.session.loggedIn == True:
                        self.head = ("303 SEE OTHER", [("location", "/")])
                        c.session.pushMessage("Hey look, you're already signed in!")

                else:
                        view = bv.noSidebarView()

                        elements = be.baseElements()
                        view["nav"] = elements.navbar()

                        view["title"] = "Login"
                        view["messages"] = bv.baseRow(c.session.getMessages())

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
                        c.session.login(name, passwd)
                        self.head = ("303 SEE OTHER", [("location", "/")])

                except Exception as exc:
                        self.head = ("303 SEE OTHER", [("location", "/auth/login")])
                        c.session.pushMessage("Something went wrong:<br>%s; plase try again." % exc, "error")


@route("/auth/logout")
class logout(basePage):
        def GET(self):
                """
                Simply log the user out. Nothing much to do here.

                redirect to login page after we're done.
                """
                c.session.logout()

                self.head = ("303 SEE OTHER", [("location", ("/auth/login"))])
