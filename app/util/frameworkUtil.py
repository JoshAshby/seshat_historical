#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
Framework Utility functions and what not

For more information, see: https://github.com/JoshAshby/

**WARNING**
Make sure you look through and change things in config.py
before running this file, to be sure it runs the way you want it to

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

class bootstrapUtil(object):
        def __init__(self, session, data={}):
                self.data = data
                self.session = session

        def buildCrumbs(self):
                trail = "<ul class=\"breadcrumb\">"
                for crumb in self.data["trail"]:
                        if crumb != self.data["trail"][-1]:
                                trail += ("<li><a href=\"%s\">%s</a></li><span class=\"divider\">/</span>" % (crumb[crumb.keys()[0]], crumb.keys()[0]))
                trail += ("<li>%s</li>" % (self.data["trail"][-1].keys()[0]))

                trail += "</ul>"
                return trail


        def buildNav(self):
                menuRegex = re.compile("(menu_)(.*)")
                nav = "<ul class=\"nav\"><li class=\"divider-vertical\"></li>"
                global urls
                for link in urls:
                        objName = link["object"].__name__
                        matchedItem = menuRegex.match(objName)
                        if matchedItem and matchedItem.groups()[0]:
                                objName = matchedItem.groups()[1]
                                active = ""
                                if objName == self.data["active"]:
                                        active = "active"
                                nav += "<li class=\"%s\"><a href=\"%s\">%s</a></li>" % (active ,link["url"], objName)
                nav += "</ul>"

                userDrop = ("Want to Login?", subURL["auth"] + "/login", "Login")
                if self.session["login"]:
                        userDrop = ("Heya, " + str(self.session["user"]), subURL["auth"] + "/logout", "Logout")

                nav += """
                <ul class="nav pull-right">
                        <li class="dropdown">
                                <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                                        %s
                                        <b class="caret"></b>
                                </a>
                                <ul class="dropdown-menu">
                                        <li><a href="%s">%s</a></li>
                                </ul>
                        </li>
                </ul>
                """ % userDrop
                return nav

        def build(self):
                return self.buildCrumbs(), self.buildNav()
