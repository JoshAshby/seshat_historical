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
        from config import *
except:
        abspath = os.path.dirname(__file__)
        sys.path.append(abspath)
        os.chdir(abspath)
        from config import *

from datetime import datetime as dt

import markdown


def postList(md=True):
        posts = []
        for key in redisPostServer.keys():
                if key[:5]=="post:":
                        post = redisPostORM(key)
                        if md:
                                post["post"] = str(markdown.markdown(post["post"]))
                        posts.append(post)

        return posts


class redisPostORM(object):
        """
        Baisc ORM style system for Posts which are stored in Redis as hashes.
        """
        def __init__(self, id=""):
                """
                Go through and either make a new post object, or if we are given a key
                which can be in the style of either a string or number, and formated as
                just the number, or like so: post:postID
                """
                self.keys = {}
                if not id:
                        try:
                                keys = redisPostServer.keys()
                                keyNum = []
                                for keyTotal in keys:
                                        keyNum.append(int(keyTotal[5:]))
                                self.id = "post:" + str(max(keyNum)+1)
                        except:
                                self.id = "post:0"
                        self.keys["author"] = ""
                        self.keys["title"] = ""
                        self.keys["time"] = dt.now()
                        self.keys["post"] = ""
                else:
                        if not id[:5] == "post:":
                                self.id = "post:" + str(id)
                        else:
                                self.id = str(id)

                        self.keys["author"] = redisPostServer.hget(self.id, "author")
                        self.keys["title"] = redisPostServer.hget(self.id, "title")
                        self.keys["time"] = redisPostServer.hget(self.id, "time")
                        self.keys["post"] = redisPostServer.hget(self.id, "post")

                self.keys["id"] = self.id[5:]

        def __getitem__(self, item):
                return self.keys[item]

        def __setitem__(self, item, value):
                self.keys[item] = value

        def cou(self):
                """
                stands for create or update since this is really a dual function function
                """
                redisPostServer.hset(self.id, "author", self.keys["author"])
                redisPostServer.hset(self.id, "title", self.keys["title"])
                redisPostServer.hset(self.id, "post", self.keys["post"])
                redisPostServer.hset(self.id, "time", dt.now())

        def delete(self):
                redisPostServer.delete(self.id)
