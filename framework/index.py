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
from route import route
from authWrap import auth

import indexView as iv

from test import *
from authController import *


@route("/")
class index(basePage):
        """
        Returns base index page.
        """
        @auth
        def GET(self):
                """

                """
                view = iv.indexView("HTML")

                self.content.put(view.build())


if __name__ == '__main__':
        """
        Because we're not doing anything else yet, such as starting a websockets
        server or whatever, we're going to just go into forever serve mode.
        """
        fw.forever()
