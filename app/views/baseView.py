#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
Base view object to use as a starting point when
building new template

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


class baseView(object):
        def __init__(self, data={"trail": ""}, replyType="HTML"):
                """

                """
                self.data = data
                self.inform = getattr(self, replyType)()

        def HTML(self):
                pass

        def JSON(self):
                pass

        def build(self):
                self.inform.nav += """
                        <ul class="nav"><li class="divider-vertical"></li>
                """
                menu = re.compile(menuRegex)
                global urls
                for url in urls:
                        match = menu.match(url["object"].__name__)
                        if "menu" in menu.findall(url["object"].__name__):
                                match = str(url["object"].__name__)
                                match = match.split("_")
                                active = ""
                                if url["object"].__name__ is self.data.__class__.__name__:
                                        active = "active"
                                self.inform.nav += """<li class="%s"><a href="%s">%s</a></li>""" % (active, url["url"], match[1])
                                self.inform.footerLinks += """| <a href="%s">%s</a> """ % (url["url"], match[1])
                self.inform.nav += """</ul>
                        <ul class="nav pull-right">
                        """
                if 0:
                        greeting = "Heya, %s!" % str(self.data.session["user"])
                        dropDown = """
                                <li class="dropdown">
                                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                                                %s
                                                <b class="caret"></b>
                                        </a>
                                        <ul class="dropdown-menu">
                                                <li><a href="%s"><i class="icon-road"></i> %s</a></li>
                                                %s
                                        </ul>
                                </li>
                        """ % (greeting, subURL["auth"] + "/logout", "Logout", "")
                        self.inform.nav += dropDown
                else:
                        self.inform.nav += """<li><a href="%s"><i class="icon-road icon-white"></i> Login</a></li>""" % (subURL["auth"] + "/login")
                self.inform.nav += """
                        </ul>
                """

                if 0:
                        self.inform.messages = self.data.session["errors"]
                else:
                        self.inform.messages = ""

                return str(self.inform)
