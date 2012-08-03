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

import authModel as am
import pickle
import string
import random


class Session(object):
        parts = ["message", "history", "username", "user_id", "level"]
        def __init__(self, sessionId):
                self.data = {}
                self.sessionId = "session:" + sessionId
                if(redisSessionServer.exists(self.sessionId)):
                        for bit in self.parts:
                                self.data[bit] = redisSessionServer.hget(self.sessionId, bit)
                else:
                        self.data = {
                                "message": "",
                                "history": [],
                                "username": "",
                                "user_id": "".join(random.choice(string.ascii_uppercase + string.digits) for x in range(10)),
                                "level": None,
                        }

        def commit(self):
                for bit in self.data:
                        redisSessionServer.hset(self.sessionId, bit, self.data[bit])
                redisSessionServer.expire(self.sessionId, 172800) #two days after last action

        def __setitem__(self, item, value):
                self.data[item] = value

        def __getitem__(self, item):
                return self.data[item]

        def __repr__(self):
                pass

        def __str__(self):
                returnData = ""
                for bit in self.data:
                        returnData += "%s : %s\n\r" % (bit, self.data[bit])
                return returnData

        def getMessage(self):
                returnData = self.data["message"]
                self.data["message"] = ""
                return returnData

        def pushMessage(self, message, messType="info"):
                if messType == "error":
                        style = """
                                <i class="icon-fire"></i> <strong>OH SNAP!!</strong><br>
                        """
                elif messType == "info":
                        style = """
                                <i class="icon-exclamation-sign"></i> <strong>Don't Panic</strong><br>
                                """
                elif messType == "success":
                        style = """
                                <i class="icon-thumbs-up">/i> <strong>WOOT!!</strong> What ever you did, it worked!!<br>
                                """
                messageTpl = """
                <div class="alert alert-%s alert-block">
                        %s
                        %s
                </div>
                """ % (messType, style, message)
                self.data["message"] += str(messageTpl)

        def login(self, user, passwd):
                userData = am.checkUser(user, passwd)
                if userData:
                        self.data["level"] = userData.perms
                        self.data["username"] = userData.name
                        self.data["users_id"] = userData.users_id
                else:
                        raise "Wrong user or password"

        def logout(self):
                self.data = {
                        "message": "",
                        "history": [],
                        "username": "",
                        "users_id": "".join(random.choice(string.ascii_uppercase)),
                        "level": None,
                }

