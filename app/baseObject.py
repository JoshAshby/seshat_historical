#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
baseObject to build pages off of

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

import re
import gevent
import models.authModel as am
import models.sessionModel as sm

import views.forms.baseForm as bf
import views.menus.baseMenu as bm
import views.baseView as bv
import views.sidebars.baseSidebar as bs


class baseHTTPPageObject(object):
        """
        Base HTTP page response object
        This determins which REQUEST method to send to,
        along with authentication level needed to access the object.
        """
        def __init__(self, env, members, sessionId):
                self.env = env
                self.members = members
                self.session = sm.Session(sessionId)
                self.method = env["REQUEST_METHOD"]

                self.status = "200 OK"
                self.headers = [
                        ("Content-type", "text/html"),
                        ]

        def sidebar(self, active=0):
                sidebarLinks = [{
                        "label": bv.baseIcon("user", "User List"),
                        "link": (subURL["admin"] + "/users")
                        }, {
                        "label": bv.baseIcon("list", "Post List"),
                        "link": (subURL["admin"] + "/posts")
                        }]

                sidebarObject = bs.baseSidebar(sidebarLinks, active)

                return sidebarObject

        def navbar(self, active=""):
                navbarLeft = [{
                        "link": "/",
                        "label": "Home",
                        "id": "home"
                        }]

                if self.session["username"]:
                        navDropdownList = [{
                                "label": bv.baseIcon("cog", "Admin"),
                                "link": (subURL["admin"] + "/")
                                }, {
                                "label": bv.baseIcon("road", "Logout"),
                                "link": (subURL["auth"] + "/logout")
                                }]


                        navDropdown = bm.baseDropdown(navDropdownList, bv.baseIcon("user", "Heya, " + self.session["username"], True))

                else:
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
                                }], action=(subURL["auth"] + "/login"), width=3)

                        navDropdownList = [{
                                "type": "form",
                                "object": loginForm
                                }]

                        navDropdown = bm.baseDropdown(navDropdownList, bv.baseIcon("user", "Heya, Stranger", True))



                navbarRight = [{
                        "type": "dropdown",
                        "object": navDropdown
                        }]

                nav = bm.baseMenu(left=navbarLeft, right=navbarRight, active=active)

                return nav

        def build(self, data, headers, status):
                content = ""
                error = False
                matches = authRegex.findall(str(self.__class__.__name__))
                if self.session["level"] == "GOD":
                        """
                        Duh, This user is obviously omnicious and has access to every
                        area in the site.
                        """
                        pass

                else:
                        level = "admin"
                        if level in matches and level != self.session["level"]:
                                self.session.pushMessage("You need to have %s rights to access this." % level, "error")
                                self.status = "303 SEE OTHER"
                                self.headers = [("location", subURL["auth"] + "/login")]
                                error = True

                if not error:
                        content = getattr(self, self.method)() or ""

                data.put(content)
                data.put(StopIteration)

                headers.put(self.headers)
                headers.put(StopIteration)

                status.put(self.status)
                status.put(StopIteration)

                self.session.commit()

        def HEAD(self):
                return self.GET()

        def GET(self):
                pass

        def POST(self):
                pass

        def PUT(self):
                pass

        def DELETE(self):
                pass
