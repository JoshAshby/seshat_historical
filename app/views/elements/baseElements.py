#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent

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

import models.sessionModel as sm

import views.menus.baseMenu as bm
import views.sidebars.baseSidebar as bs
import views.lists.baseList as bl
import views.forms.baseForm as bf
import views.baseView as bv


class baseElements(object):
        def __init__(self, sessionID, nav="", sidebar=0):
                self.session = sm.Session(sessionID)
                self.navActive = nav
                self.sidebarActive = sidebar

        def sidebar(self):
                pass

        def navbar(self):
                navbarLeft = [{
                        "link": "/",
                        "label": "Home",
                        "id": "home"
                        }]

                if self.session["username"]:
                        navDropdownList = [{
                                "label": bv.baseIcon("cog", "Admin"),
                                "link": ("/admin/")
                                }, {
                                "label": bv.baseIcon("road", "Logout"),
                                "link": ("/auth/logout")
                                }]


                        navDropdown = bm.baseDropdown(navDropdownList, bv.baseIcon("user", "Heya, " + self.session.username, True))

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
                                }], action=("/auth/login"), width=3)

                        navDropdownList = [{
                                "type": "form",
                                "object": loginForm
                                }]

                        navDropdown = bm.baseDropdown(navDropdownList, bv.baseIcon("user", "Heya, Stranger", True))



                navbarRight = [{
                        "type": "dropdown",
                        "object": navDropdown
                        }]

                nav = bm.baseMenu(left=navbarLeft, right=navbarRight, active=self.navActive)

                return nav


class adminElements(baseElements):
        def sidebar(self):
                sidebarLinks = [{
                        "label": bv.baseIcon("user", "User List"),
                        "link": ("/admin/users")
                        }, {
                        "label": bv.baseIcon("list", "Post List"),
                        "link": ("/admin/posts")
                        }]

                sidebarObject = bs.baseSidebar(sidebarLinks, self.sidebarActive)

                return sidebarObject
