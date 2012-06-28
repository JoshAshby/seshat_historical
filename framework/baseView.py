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


class baseView(object):
        def __init__(self, replyType="HTML", data={}):
                """

                """
                self.inform = getattr(self, replyType)()
                self.data = data

        def HTML(self):
                pass

        def JSON(self):
                pass

        def build(self):
                return str(self.inform)

