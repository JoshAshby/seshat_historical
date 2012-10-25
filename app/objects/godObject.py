#!/usr/bin/env python
"""
Seshat
Web App/API framework built on top of gevent
baseObject to build pages off of

For more information, see: https://github.com/JoshAshby/

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import config as c
import seshat.baseObject as bo


class godObject(bo.baseHTTPPageObject):
       __level__ = "GOD"
       __login__ = True
       __name__ = "god"
