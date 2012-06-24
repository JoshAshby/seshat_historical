#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
Main index file.

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


@route("/")
class index(basePage):
        """
        This routes to the root URL

        Pages can be generators and use the yield statement
        such as shown here.
        """
        def GET(self):
                for i in range(1,101):
                        yield ("%i<br>" % i)


@route("/session/")
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
                if not self.session.has_key('id'):
                        self.session['id'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
                        return None
                else:
                        return str(self.session['id'])


@route("/members/(.*)/")
class members(basePage):
        """
        Finally, URL's can have place holders that are matched.
        These can be found in self.members with numbers, corrisponding
        to the placement in the URL. These place holders are simply
        regex strings, such as (.*)

        for example, /members/(.*)/ will have one
                number in self.members, 0. This is because the 
                placement of the (.*) matched regex is at 0

        self.members also includes any query strings appended to 
        the URL.
        Try loading this page as: /members/Hello/?query=Dog&search=Fred+Jones
        """
        def GET(self):
                self.data = ''

                for member in self.members:
                        self.data += ("<h1>%s : %s</h1>" % (str(member), str(self.members[member])))

                for bit in self.env:
                        self.data += ("%s : %s<br>" % (str(bit), str(self.env[bit])))

                return self.data


if __name__ == '__main__':
        fw.forever()
