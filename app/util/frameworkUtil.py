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


class bootstrapUtil(object):
        def __init__(self, data={}):
                self.data = data

        def buildCrumbs(self):
                trail = "<ul class=\"breadcrumb\">"
                for crumb in self.data["trail"]:
                        trail += ("<li><a href=\"%s\">%s</a></li> <span class=\"divider\">/</span>" % (self.data["trail"][crumb], crumb))
                trail += "</ul>"
                return trail


        def buildNav(self):
                nav = "<ul class=\"nav\"><li class=\"divider-vertical\"></li>"
                for link in self.data["nav"]:
                        active = ""
                        if self.data["nav"][link] == self.data["active"]:
                                active = "active"
                        nav += "<li class=\"%s\"><a href=\"%s\">%s</a></li>" % (active ,self.data["nav"][link], link)
                nav += "</ul>"
                if self.data["login"]:
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
                        """ % ("Login", "/admin/logou", "Logout")
                return nav

        def build(self):
                return self.buildCrumbs(), self.buildNav()
