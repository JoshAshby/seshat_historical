#!/usr/bin/env python
"""
Seshat
Web App/API framework built on top of gevent
Mainenance Controller

For more information, see: https://github.com/JoshAshby/

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import config as c
import seshat.baseObject as bo
import seshat.baseView as bv
from seshat.route import route


@route("/(.*)")
class maintenance(bo.baseHTMLObject):
        """
        Returns base maintenance page
        """
        def GET(self):
                """

                """
                self.view = "Down"
