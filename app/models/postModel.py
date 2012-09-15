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


class basePost(object):
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

        def commit(self):
                for bit in self.parts:
                        c.redisPostServer.hset("post:"+self.id, bit, getattr(self, bit))

        def __str__(self):
                reply = ""
                for part in self.parts:
                         reply += "%s: "%(part) + getattr(self, part) + "\r\n"

                return reply

        def __repr__(self):
                reply = ""
                for part in self.parts:
                         reply += "%s: "%(part) + getattr(self, part) + "\r\n"

                return reply

        def __getattr__(self, item):
                return object.__getattribute__(self, item)

        def __getitem__(self, item):
                return object.__getattribute__(self, item)

        def __setattr__(self, item, value):
                return object.__setattr__(self, item, value)

        def __setitem__(self, item, value):
                return object.__setattr__(self, item, value)

        def delete(self):
                c.redisPostServer.delete("post:"+self.id)
