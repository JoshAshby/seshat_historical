#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
Database model for authentication and users

For more information, see: https://github.com/JoshAshby/

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import sys, os

try:
        import config as c
except:
        abspath = os.path.dirname(__file__)
        sys.path.append(abspath)
        os.chdir(abspath)
        import config as c

from datetime import datetime as dt
import models.baseModel as bm

import markdown
import string
import random


def postList(md=True):
        posts = []
        for key in c.redisPostServer.keys():
                if key[:5]=="post:":
                        post = basePost(key[5:])
                        if md:
                                try:
                                        post["post"] = str(markdown.markdown(post["post"]))

                                except:
                                        pass
                        posts.append(post)

        return posts


class basePost(bm.baseModel):
        __dbname__ = "redisPostServer"
        __dbid__ = "post:"
        parts = ["author", "title", "post", "time", "id"]

        def __init__(self, id=None):
                self.id = id

                if(self.id and c.redisPostServer.exists("post:"+self.id)):
                        for bit in self.parts:
                                setattr(self, bit, c.redisPostServer.hget("post:"+self.id, bit))
                                self.id = id

                else:
                        #Post doesn't exist, so create a blank post object
                        for bit in self.parts:
                                setattr(self, bit, None)
                                self.time = dt.utcnow().strftime("%b-%d-%Y %I:%M %p")
                                self.id = "".join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
