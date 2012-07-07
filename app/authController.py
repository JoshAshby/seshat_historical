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
import util.frameworkUtil as fwUtil
from baseObject import baseHTTPPageObject as basePage
from seshat.route import route
import views.authView as av
import models.authModel as am


@route(subURL["auth"] + "/")
class auth_Home(basePage):
        def GET(self):
                """
                """
                view = av.indexView(data=self)

                return view.build()


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
                        view = av.loginView(data=self)

                        return view.build()

        def POST(self):
                """
                Use form data to check login, and the redirect if successful
                if not redirect to login page again.
                """
                passwd = self.members["passwd"]
                name = self.members["user"]

                try:
                        self.session.login(name, passwd)
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", baseURL + "/")]
                except:
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", baseURL + subURL["auth"] + "/login")]
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
                self.headers = [("location", (subURLLink["auth"] + "/login"))]

                return ""


@route(subURL["auth"] + "/newUser")
class auth_NewUser_admin(basePage):
        def GET(self):
                """
                This will eventually give a nice form in order to
                make a new user, right now it does nothing however.
                """
                self.permList = am.permList()
                view = av.newUserView(data=self)

                return view.build()


        def POST(self):
                """

                """
                name = self.members["user"]
                password = self.members["passwd"]
                perms = self.members["perms"]
                notes = self.members["notes"]
                try:
                        am.newUser(name, password, perms, notes)
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", (subURLLink["auth"] + "/newUser"))]
                        self.session.pushMessage(("Congrats! The user %s was created!" % name))
                except:
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", (subURLLink["auth"] + "/newUser"))]
                        self.passError("The user name %s is already in use. Sorry!"%self.members["alreadyUsed"])
                return ""


@route(subURL["auth"] + "/userList")
class auth_userList_admin_menu(basePage):
        def GET(self):
                """

                """
                self.users = am.userList()
                self.permList = am.permList()

                view = av.userListView(data=self)

                return view.build()



@route(subUTL["auth"] + "/updateUser")
class auth_updateUser_admin(basePage):
        def POST(self):
                """
                """
                name = self.members["user"]
                perms = self.members["perms"]
                notes = self.members["notes"]
                try:
                        am.updateUser(name, perms, notes)
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", (subURLLink["auth"] + "/userList"))]
                        self.session.pushMessage(("Congrats! The user %s was updated!" % name))
                except:
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", (subURLLink["auth"] + "/newUser"))]
                        self.passError("The user name %s is already in use. Sorry!"%self.members["alreadyUsed"])
                return ""
