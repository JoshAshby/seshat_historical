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

import seshat.framework as fw
import util.frameworkUtil as fwUtil
from baseObject import baseHTTPPageObject as basePage
from seshat.route import route
from auth.authWrap import auth

import views.indexView as iv

from testController import *
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
                elementUnits = {"trail": {"Home": "/"}}
                elementObject = fwUtil.bootstrapUtil(elementUnits)
                trailUnit = elementObject.buildCrumbs()

                view = iv.indexView(data={"trail": trailUnit, "nav": ""})

                self.content.put(view.build())


if __name__ == '__main__':
        """
        Because we're not doing anything else yet, such as starting a websockets
        server or whatever, we're going to just go into forever serve mode.
        """
        fw.forever()
