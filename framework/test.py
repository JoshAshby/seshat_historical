#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
Test/utility pages file.

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

import framework as fw
from baseObject import baseHTTPPageObject as basePage
from route import *
import random
import string


subURL = "/test"


@route(subURL + "/members/(.*)/")
class members(basePage):
        """
        URL's can have place holders that are matched.
        These can be found in self.members with numbers, corrisponding
        to the placement in the URL. These place holders are simply
        regex strings, such as (.*)

        for example, /test/members/(.*)/ will have one
                number in self.members, 0. This is because the 
                placement of the (.*) matched regex is at 0

        self.members also includes any query strings appended to 
        the URL.
        Try loading this page as: /test/members/Hello/?query=Dog&search=Fred+Jones
        """
        def GET(self):
                self.data = ""

                for member in self.members:
                        self.data += ("<h1>%s : %s</h1>" % (str(member), str(self.members[member])))

                for bit in self.env:
                        self.data += ("%s : %s<br>" % (str(bit), str(self.env[bit])))

                return self.data



@route(subURL + "/session")
@route(subURL + "/session/")
class session(basePage):
        """
        Pages can also be static and return their content
        all at once, or they can return None.
        """
        def GET(self):
                """
                Sessions can be used and access from inside each
                page such as shwon here.
                """
                self.session["login"] = True
                if not self.session.has_key("test"):
                        self.session["test"] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
                        return "Set"
                else:
                        return str(self.session["test"])
