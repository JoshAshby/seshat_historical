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

import views.adminView as av

import models.authModel as am
import models.postModel as pm

import re


@route(subURL["admin"] + "/")
class adminIndex_admin(basePage):
        def GET(self):
                """
                """
                view = av.indexView(data=self)

                return view.build()


@route(subURL["admin"] + "/users/new")
class userNew_admin(basePage):
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
                        self.headers = [("location", (subURL["admin"] + "/users/new"))]
                        self.session.pushMessage(("Congrats! The user %s was created!" % name))
                except:
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", (subURL["admin"] + "/users/new"))]
                        self.session.pushMessage(("The user name %s is already in use. Sorry!" % name), "error")
                return ""


@route(subURL["admin"] + "/users/")
class userIndex_admin(basePage):
        def GET(self):
                """

                """
                self.users = am.userList()
                self.permList = am.permList()

                view = av.userListView(data=self)

                return view.build()


        def POST(self):
                """
                """
                id = self.members["id"]
                name = self.members["user"]
                perms = self.members["perms"]
                notes = self.members["notes"]
                try:
                        am.updateUser(id, name, perms, notes)
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", (subURL["admin"] + "/users/"))]
                        self.session.pushMessage(("Congrats! The user %s was updated!" % name))
                except:
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", (subURL["admin"] + "/users/"))]
                        self.session.pushMessage(("The user name %s is already in use. Sorry!" % name), "error")
                return ""


@route(subURL["admin"] + "/posts/")
class postsIndex_admin(basePage):
        def GET(self):
                """
                """
                self.posts = pm.postList()
                view = av.postListView(data=self)

                return view.build()

        def POST(self):
                """
                """
                title = self.members["title"]
                post = self.members["post"]

                im.newPost(title, post, self.session["username"])
                self.status = "303 SEE OTHER"
                self.headers = [("location", (subURL["admin"] + "/posts/"))]
                self.session.pushMessage(("Congrats! The post %s was created!" % title))
                return ""
