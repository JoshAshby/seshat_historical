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
from objects.userObject import userObject as basePage
from seshat.route import route

import models.postModel as pm

import views.baseView as bv
import views.lists.baseList as bl

@route("/")
class index(basePage):
        __menu__ = "Home"
        """
        Returns base index page.
        """
        def GET(self):
                """

                """
                posts = pm.postList()

                view = bv.noSidebarView()

                view["nav"] = "Home"
                view["title"] = "Home"

                postList = bl.baseList(posts, "post_index")

                view["content"] = bv.baseRow(postList)

                return view.build()


#from authController import *
#from adminController import *


if __name__ == '__main__':
        """
        Because we're not doing anything else yet, such as starting a websockets
        server or whatever, we're going to just go into forever serve mode.
        """
        fw.forever()
