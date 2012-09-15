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

from objects.adminObject import adminObject as basePage
from objects.userObject import userObject as setupPage
from seshat.route import route

import models.authModel as am
import models.postModel as pm

import views.baseView as bv
import views.lists.baseList as bl
import views.forms.baseForm as bf

import urllib

import views.elements.baseElements as be


@route("/admin")
class adminIndex_admin(basePage):
        def GET(self):
                """
                """
                view = bv.sidebarView()

                elements = be.adminElements()
                view["nav"] = elements.navbar()
                view["sidebar"] = elements.sidebar()

                view["title"] = "Admin Panel"
                view["messages"] = bv.baseRow(c.session.getMessages(), 12, 0)

                view["content"] = "Well you have nothing to do here, but you might want to take a look over at the sidebar for somethings to do..."

                return view.build()


@route("/admin/users")
class usersIndex_admin(basePage):
        def GET(self):
                """

                """
                users = am.userList()

                view = bv.sidebarView()

                elements = be.adminElements()
                view["nav"] = elements.navbar()
                view["sidebar"] = elements.sidebar()

                view["title"] = "Users"
                view["messages"] = bv.baseRow(c.session.getMessages(), 12, 0)

                pageHead = """What to <a href="%s">add a user?</a>""" % ("/admin/users/new")

                if users:
                        userList = bl.baseList(users, "row_list_User")

                        content = bv.baseRow(userList, 8, 0)

                else:
                        content = "Well either all of your users have god perms and aren't shown, or you don't have any additional users!"

                view["content"] = bv.baseRow([pageHead, content], 8, 0)

                return view.build()


@route("/admin/users/edit/(.*)")
class usersEdit_admin(basePage):
        def GET(self):
                """
                """
                id = self.members[0]
                user = am.baseUser(id)

                view = bv.sidebarView()

                elements = be.adminElements()
                view["nav"] = elements.navbar()
                view["sidebar"] = elements.sidebar()

                view["title"] = "Edit User " + user.username
                view["messages"] = bv.baseRow(c.session.getMessages(), 12, 0)

                editForm = bf.baseForm(fields=[{
                        "name": "username",
                        "value": user["username"]
                        }, {
                        "name": "password",
                        "type": "password",
                        "placeholder": "New Password"
                        }, {
                        "name": "notes",
                        "type": "textarea",
                        "value": user["notes"]
                        }, {
                        "name": "submit",
                        "type": "submit",
                        "value": "Update"
                        }], action=("/admin/users/edit/" + id))

                view["content"] = bv.baseRow(editForm, offset=0)

                return view.build()

        def POST(self):
                """
                """
                id = self.members[0]
                name = self.members["username"] or ""
                perms = self.members["perms"] or "normal"
                notes = self.members["notes"] or ""

                try:
                        user = am.userBase(id)
                        user["username"] = name
                        user["level"] = perms
                        user["notes"] = notes

                        if self.members["password"]:
                                user.paassword = self.members["password"]

                        user.commit()

                        self.head = ("303 SEE OTHER", [("location", "/admin/users")])
                        c.session.pushMessage(("Congrats! The user %s was updated!" % name))

                except:
                        self.head = ("303 SEE OTHER", [("location", "/admin/users")])
                        c.session.pushMessage(("The user name %s is already in use. Sorry!" % name), "error")


@route("/admin/users/new")
class usersNew_admin(basePage):
        def GET(self):
                """
                This gives a nice little list of all the users in the system, 
                with the exception of users marked as having GOD level.
                """
                view = bv.sidebarView()

                elements = be.adminElements()
                view["nav"] = elements.navbar()
                view["sidebar"] = elements.sidebar()

                view["title"] = "Adding a new User"
                view["messages"] = bv.baseRow(c.session.getMessages(), 12, 0)

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
                        }], action="/admin/users/new")

                view["content"] = bv.baseRow(editForm, offset=0)

                return view.build()

        def POST(self):
                """

                """
                name = self.members["username"]
                perms = self.members["perms"] or "normal"
                notes = self.members["notes"] or ""
                try:
                        user = am.baseUser()
                        user["username"] = name
                        user["level"] = perms
                        user["notes"] = notes
                        user.paassword = self.members["password"]

                        user.commit()

                        self.head = ("303 SEE OTHER", [("location", "/admin/users/new")])
                        c.session.pushMessage(("Congrats! The user %s was created!" % name))
                except:
                        self.head = ("303 SEE OTHER", [("location", "/admin/users/new")])
                        c.session.pushMessage(("The user name %s is already in use. Sorry!" % name), "error")


@route("/admin/posts")
class postsIndex_admin(basePage):
        def GET(self):
                """
                """
                posts = pm.postList()

                view = bv.sidebarView()

                elements = be.adminElements()
                view["nav"] = elements.navbar()
                view["sidebar"] = elements.sidebar()

                view["title"] = "Posts"
                view["messages"] = bv.baseRow(c.session.getMessages(), 12, 0)

                pageHead = """Want to <a href="%s">add another post?</a>""" % ("/admin/posts/new")

                if posts:
                        postList = bl.baseList(posts, "row_list_Post")

                        content = bv.baseRow(postList, 8, 0)

                else:
                        content = "You don't have any posts at this time!"

                view["content"] = bv.baseRow([pageHead, content], 8, 0)

                return view.build()


@route("/admin/posts/edit/(.*)")
class postsEdit_admin(basePage):
        def GET(self):
                """
                """
                id = self.members[0]

                post = pm.basePost(id)

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
                        }], action=("/admin/posts/edit/" + id))

                view = bv.sidebarView()

                elements = be.adminElements()
                view["nav"] = elements.navbar()
                view["sidebar"] = elements.sidebar()

                view["title"] = "Edit Post" + id
                view["messages"] = bv.baseRow(c.session.getMessages(), 12, 0)

                view["content"] = bv.baseRow(editForm, offset=0)

                return view.build()

        def POST(self):
                """
                """
                id = self.members[0]
                title = self.members["title"]
                post = urllib.unquote(self.members["post"])

                updatePost = pm.basePost(id)

                updatePost["title"] = title
                updatePost["post"] = post
                updatePost["author"] = c.session.user.username

                updatePost.commit()

                self.head = ("303 SEE OTHER", [("location", "/admin/posts")])
                c.session.pushMessage(("Congrats! The post %s was updated!" % title))


@route("/admin/posts/new")
class postsNew_admin(basePage):
        def GET(self):
                """
                """
                view = bv.sidebarView()

                elements = be.adminElements()
                view["nav"] = elements.navbar()
                view["sidebar"] = elements.sidebar()

                view["title"] = "Adding a new Post"
                view["messages"] = bv.baseRow(c.session.getMessages(), 12, 0)

                editForm = bf.baseForm(fields=[{
                        "name": "title",
                        }, {
                        "name": "post",
                        "type": "textarea"
                        }, {
                        "name": "submit",
                        "type": "submit",
                        "value": "Create"
                        }], action="/admin/posts/new")

                view["content"] = bv.baseRow(editForm, offset=0)

                return view.build()

        def POST(self):
                """
                """
                title = self.members["title"]
                post = urllib.unquote(self.members["post"])

                newPost = pm.basePost()

                newPost["title"] = title
                newPost["post"] = post
                newPost["author"] = c.session.user.username

                newPost.commit()

                self.head = ("303 SEE OTHER", [("location", "/admin/posts")])
                c.session.pushMessage(("Congrats! The post %s was created!" % title))



import bcrypt
@route("/setup")
class setup(setupPage):
        def GET(self):
                """
                """
                user = am.baseUser()
                user["username"] = "Josh"
                user["level"] = "GOD"
                user["notes"] = ""
                user.password = "josh"

                user.commit()

                print user.password, bcrypt.hashpw("josh", user.password)

                view = bv.noSidebarView()

                elements = be.baseElements()
                view["nav"] = elements.navbar()

                view["title"] = "Initial Setup"
                view["messages"] = bv.baseRow(c.session.getMessages(), 12, 0)

                view["content"] = "User Josh with password josh has been created."

                return view.build()
