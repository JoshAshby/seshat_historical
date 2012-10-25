#!/usr/bin/env python
"""
Seshat
Web App/API framework built on top of gevent
Main index file.

For more information, see: https://github.com/JoshAshby/

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import config as c

from objects.userObject import userObject as basePage
from seshat.route import route


@route("/")
class index(basePage):
        __menu__ = "Home"
        """
        Returns base index page.
        """
        def GET(self):
                """

                """
                self.view = "Hi there"
