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

import models.authModel as am
import models.postModel as pm

import views.baseView as bv

import urllib


@route(subURL["admin"] + "/")
class adminIndex_admin(basePage):
        def GET(self):
                """
                """
                view = bv.sidebarView()

                return view.build()


@route(subURL["admin"] + "/users/new")
class usersNew_admin(basePage):
        def GET(self):
                """
                This gives a nice little list of all the users in the system, 
                with the exception of users marked as having GOD level.
                """
                self.permList = am.permList()
                view = bv.sidebarView()

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
class usersIndex_admin(basePage):
        def GET(self):
                """

                """
                self.users = am.userList()
                self.permList = am.permList()

                view = bv.sidebarView()

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
                self.posts = pm.listPosts()
                view = bv.sidebarView()

                return view.build()

        def POST(self):
                """
                """
                id = self.members["id"]
                title = self.members["title"]
                post = urllib.unquote(self.members["post"])

                updatePost = pm.RedisPostORM(id)

                updatePost.title = title
                updatePost.post = post
                updatePost.author = self.session["username"]

                updatePost.cou()

                self.status = "303 SEE OTHER"
                self.headers = [("location", (subURL["admin"] + "/posts/"))]
                self.session.pushMessage(("Congrats! The post %s was updated!" % title))
                return ""


@route(subURL["admin"] + "/posts/new")
class postsNew_admin(basePage):
        def GET(self):
                """
                """
                view = bv.sidebarView()

                return view.build()

        def POST(self):
                """
                """
                title = self.members["title"]
                post = urllib.unquote(self.members["post"])

                newPost = pm.RedisPostORM()

                newPost.title = title
                newPost.post = post
                newPost.author = self.session["username"]

                newPost.cou()
                self.status = "303 SEE OTHER"
                self.headers = [("location", (subURL["admin"] + "/posts/"))]
                self.session.pushMessage(("Congrats! The post %s was created!" % title))
                return ""
