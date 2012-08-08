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
import views.lists.baseList as bl
import views.forms.baseForm as bf

import urllib


@route(subURL["admin"] + "/")
class adminIndex_admin(basePage):
        def GET(self):
                """
                """
                view = bv.sidebarView()
                view["nav"] = self.navbar()
                view["title"] = "Admin Panel"
                view["messages"] = bv.baseRow(self.session.getMessage())

                view["sidebar"] = self.sidebar()

                view["content"] = "Well you have nothing to do here, but you might want to take a look over at the sidebar for somethings to do..."

                return view.build()


@route(subURL["admin"] + "/users")
class usersIndex_admin(basePage):
        def GET(self):
                """

                """
                users = am.userList()

                view = bv.sidebarView()
                view["nav"] = self.navbar()
                view["sidebar"] = self.sidebar()
                view["title"] = "Users"
                view["messages"] = bv.baseRow(self.session.getMessage())

                if users:
                        userList = bl.baseList(users, "row_list_User")

                        view["content"] = bv.baseRow(userList, 8, 0)

                else:
                        view["content"] = "Well either all of your users have god perms and aren't shown, or you don't have any additional users!"

                return view.build()


@route(subURL["admin"] + "/users/edit/(.*)")
class usersEdit_admin(basePage):
        def GET(self):
                """
                """
                id = self.members[0]
                user = am.redisUserORM(id)

                view = bv.sidebarView()
                view["nav"] = self.navbar()
                view["sidebar"] = self.sidebar()
                view["title"] = "Edit User " + id
                view["messages"] = bv.baseRow(self.session.getMessage())

                editForm = bf.baseForm(fields=[{
                        "name": "username",
                        "value": user["username"]
                        }, {
                        "name": "password",
                        "type": "password",
                        "value": user["password"]
                        }, {
                        "name": "notes",
                        "type": "textarea",
                        "value": user["notes"]
                        }, {
                        "name": "submit",
                        "type": "submit",
                        "value": "Update"
                        }], action=(subURL["admin"]+"/users/new"))

                view["content"] = bv.baseRow(editForm, offset=0)

                return view.build()

        def POST(self):
                """
                """
                id = self.members[0]
                name = self.members["user"] or ""
                perms = self.members["perms"] or "normal"
                notes = self.members["notes"] or ""
                try:
                        user = redisUserORM(id)
                        user["username"] = name
                        user["perms"] = perms
                        user["notes"] = notes

                        user.cou()

                        self.status = "303 SEE OTHER"
                        self.headers = [("location", (subURL["admin"] + "/users/"))]
                        self.session.pushMessage(("Congrats! The user %s was updated!" % name))
                except:
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", (subURL["admin"] + "/users/"))]
                        self.session.pushMessage(("The user name %s is already in use. Sorry!" % name), "error")


@route(subURL["admin"] + "/users/new")
class usersNew_admin(basePage):
        def GET(self):
                """
                This gives a nice little list of all the users in the system, 
                with the exception of users marked as having GOD level.
                """
                view = bv.sidebarView()
                view["sidebar"] = self.sidebar()
                view["nav"] = self.navbar()
                view["title"] = "Adding a new User"
                view["messages"] = bv.baseRow(self.session.getMessage())

                editForm = bf.baseForm(fields=[{
                        "name": "username",
                        "placeholder": "Username"
                        }, {
                        "name": "password",
                        "type": "password",
                        "placeholder": "Password"
                        }, {
                        "name": "notes",
                        "type": "textarea"
                        }, {
                        "name": "submit",
                        "type": "submit",
                        "value": "Update"
                        }], action=(subURL["admin"]+"/users/new"))

                view["content"] = bv.baseRow(editForm)

                return view.build()

        def POST(self):
                """

                """
                name = self.members["user"]
                perms = self.members["perms"] or "normal"
                notes = self.members["notes"] or ""
                try:
                        user = redisUserORM()
                        user["username"] = name
                        user["perms"] = perms
                        user["notes"] = notes

                        user.cou()

                        self.status = "303 SEE OTHER"
                        self.headers = [("location", (subURL["admin"] + "/users/new"))]
                        self.session.pushMessage(("Congrats! The user %s was created!" % name))
                except:
                        self.status = "303 SEE OTHER"
                        self.headers = [("location", (subURL["admin"] + "/users/new"))]
                        self.session.pushMessage(("The user name %s is already in use. Sorry!" % name), "error")


@route(subURL["admin"] + "/posts")
class postsIndex_admin(basePage):
        def GET(self):
                """
                """
                posts = pm.postList()

                view = bv.sidebarView()
                view["nav"] = self.navbar()
                view["sidebar"] = self.sidebar()
                view["title"] = "Posts"
                view["messages"] = bv.baseRow(self.session.getMessage())

                if posts:
                        postList = bl.baseList(posts, "row_list_Post")

                        view["content"] = bv.baseRow(postList, 8, 0)

                else:
                        view["content"] = "You don't have any posts at this time!"

                return view.build()


@route(subURL["admin"] + "/posts/edit/(.*)")
class postsEdit_admin(basePage):
        def GET(self):
                """
                """
                id = self.members[0]

                post = pm.redisPostORM(id)

                editForm = bf.baseForm(fields=[{
                        "name": "title",
                        "value": post["title"]
                        }, {
                        "name": "post",
                        "value": post["post"],
                        "type": "textarea"
                        }, {
                        "name": "submit",
                        "type": "submit",
                        "value": "Update"
                        }], action=(subURL["admin"]+"/posts/edit/"+id))

                view = bv.noSidebarView()
                view["nav"] = self.navbar()
                view["title"] = "Edit Post" + id
                view["messages"] = bv.baseRow(self.session.getMessage())

                view["content"] = bv.baseRow(editForm)

                return view.build()

        def POST(self):
                """
                """
                id = self.members["id"]
                title = self.members["title"]
                post = urllib.unquote(self.members["post"])

                updatePost = pm.redisPostORM(id)

                updatePost.title = title
                updatePost.post = post
                updatePost.author = self.session["username"]

                updatePost.cou()

                self.status = "303 SEE OTHER"
                self.headers = [("location", (subURL["admin"] + "/posts/"))]
                self.session.pushMessage(("Congrats! The post %s was updated!" % title))


@route(subURL["admin"] + "/posts/new")
class postsNew_admin(basePage):
        def GET(self):
                """
                """
                view = bv.sidebarView()
                view["nav"] = self.navbar()
                view["sidebar"] = self.sidebar()
                view["title"] = "Adding a new Post"
                view["messages"] = bv.baseRow(self.session.getMessage())

                editForm = bf.baseForm(fields=[{
                        "name": "title",
                        }, {
                        "name": "post",
                        "type": "textarea"
                        }, {
                        "name": "submit",
                        "type": "submit",
                        "value": "Create"
                        }], action=(subURL["admin"]+"/posts/new"))

                view["content"] = bv.baseRow(editForm)

                return view.build()

        def POST(self):
                """
                """
                title = self.members["title"]
                post = urllib.unquote(self.members["post"])

                newPost = pm.redisPostORM()

                newPost.title = title
                newPost.post = post
                newPost.author = self.session["username"]

                newPost.cou()
                self.status = "303 SEE OTHER"
                self.headers = [("location", (subURL["admin"] + "/posts/"))]
                self.session.pushMessage(("Congrats! The post %s was created!" % title))
