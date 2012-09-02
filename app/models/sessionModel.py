#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
baseObject to build pages off of

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

import authModel as am
import pickle
import string
import random

import bcrypt


class Session(object):
        parts = ["message", "history", "username", "user_id", "level"]
        def __init__(self, id):
                self.id = "session:" + id

                if(c.redisSessionServer.exists(self.id)):
                        for bit in self.parts:
                                setattr(self, bit, c.redisSessionServer.hget(self.id, bit))
                else:
                        self.message = ""
                        self.history = []
                        self.username = ""
                        self.user_id = "".join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
                        self.level = None

        def commit(self):
                for bit in self.parts:
                        c.redisSessionServer.hset(self.id, bit, getattr(self, bit))
                c.redisSessionServer.expire(self.id, 172800) #two days after last action

        def __str__(self):
                returnData = ""
                for bit in self:
                        returnData += "%s : %s\n\r" % (bit, getattr(self, bit))
                return returnData

        def __getattr__(self, item):
                return getattr(self, item)

        def __getitem__(self, item):
                return getattr(self, item)

        def __setattr__(self, item, value):
                return object.__setattr__(self, item, value)

        def __setitem__(self, item, value):
                return object.__setattr__(self, item, value)

        def gm(self):
                return self.getMessage()

        def pm(self, message, messType):
                return self.pushMessage(message, messType)

        def getMessage(self):
                returnData = self.message
                self.message = ""
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
                self.message += str(messageTpl)

        def login(self, username, passwd):
                user = am.findUser(username)
                if user:
                        if user["password"] == bcrypt.hashpw(passwd, user["password"]):
                                self.level = user["perm"]
                                self.username = user["username"]
                                self.users_id = user["key"]
                        else:
                                raise "We're sorry, your password appears to be wrong."
                else:
                        raise "We're sorry, we can't find that username in our system."

        def logout(self):
                self.message = ""
                self.history = []
                self.username = ""
                self.user_id = "".join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
                self.level = None

