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

import bcrypt

def userList():
        users = []
        for key in redisUserServer.keys():
                if key[:5] == "user:":
                        users.append(redisUserORM(key))

        return users

def findUser(username):
        names = []
        for key in userList():
                if key["username"] == username:
                        return key


class redisUserORM(object):
        def __init__(self, id=""):
                self.keys = {}
                if not id:
                        try:
                                keys = redisUserServer.keys()
                                keyNum = []
                                for keyTotal in keys:
                                        keyNum.append(int(keyTotal[5:]))
                                self.id = "user:" + str(max(keyNum)+1)
                        except:
                                self.id = "user:0"

                        self.keys["username"] = ""
                        self.keys["password"] = ""
                        self.keys["notes"] = dt.now()
                        self.keys["perm"] = ""
                else:
                        if not id[:5] == "user:":
                                self.id = "user:" + str(id)
                        else:
                                self.id = str(id)

                        self.keys["username"] = redisPostServer.hget(self.id, "username")
                        self.keys["password"] = redisPostServer.hget(self.id, "password")
                        self.keys["notes"] = redisPostServer.hget(self.id, "notes")
                        self.keys["perm"] = redisPostServer.hget(self.id, "perm")

                        self.keys["id"] = self.id[5:]

        def __getitem__(self, item):
                return self.keys[item]

        def __setitem__(self, item, value):
                if item == "password":
                        value = bcrypt.hashpw(value, bcrypt.gensalt())
                self.keys[item] = value

        def cou(self):
                if findUser(self.keys["username"]):
                        raise "Username already in use"
                redisPostServer.hset(self.id, "username", self.keys["username"])
                redisPostServer.hset(self.id, "password", self.keys["password"])
                redisPostServer.hset(self.id, "notes", self.keys["notes"])
                redisPostServer.hset(self.id, "perm", self.keys["perm"])

        def delete(self):
                redisUserServer.delete(self.id)
