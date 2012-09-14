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

import string
import random

import bcrypt


def userList():
        users = []
        for key in c.redisUserServer.keys():
                if key[:5] == "user:":
                        users.append(baseUser(key[5:]))
        return users

def findUser(username):
        names = []
        for key in userList():
                if key.username == username:
                        return key


class baseUser(object):
        parts = ["username", "level", "password", "notes", "level"]
        def __init__(self, id=None):
                self.id = id

                if(self.id and c.redisUserServer.exists("user:"+self.id)):
                        for bit in self.parts:
                                setattr(self, bit, c.redisUserServer.hget("user:"+self.id, bit))
                else:
                        #User doesn't exist, so create a blank user object
                        self.id = "".join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))

                        for bit in self.parts:
                                setattr(self, bit, None)

        def commit(self):
                for bit in self.parts:
                        c.redisUserServer.hset("user:"+self.id, bit, getattr(self, bit))

        def __getattr__(self, item):
                return object.__getattribute__(self, item)

        def __getitem__(self, item):
                return object.__getattribute__(self, item)

        def __setattr__(self, item, value):
                if item == "password" and value:
                        value = bcrypt.hashpw(value, bcrypt.gensalt())

                return object.__setattr__(self, item, value)

        def __setitem__(self, item, value):
                if item == "password" and value:
                        value = bcrypt.hashpw(value, bcrypt.gensalt())

                return object.__setattr__(self, item, value)

        def delete(self):
                c.redisUserServer.delete("user:"+self.id)
