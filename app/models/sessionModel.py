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

import string
import random
import bcrypt

import models.authModel as am
import models.baseModel as bm


class session(bm.baseModel):
        __dbname__ = "redisSessionServer"
        __dbid__ = "session:"
        parts = ["history", "userID", "messages", "loggedIn"]
        def __init__(self, id):
                self.id = id

                if(getattr(c, self.__dbname__).exists(self.__dbid__+self.id)):
                        for bit in self.parts:
                                setattr(self, bit, getattr(c, self.__dbname__).hget(self.__dbid__+self.id, bit))

                        self.user = am.baseUser(self.userID)
                else:
                        #No session was found so make a new one
                        for bit in self.parts:
                                setattr(self, bit, None)
                                self.messages = ""
                                self.history = ""
                                self.loggedIn = False

                        self.user = am.baseUser()

        def getMessages(self):
                returnData = self.messages
                self.messages = ""
                return returnData

        def pushMessage(self, message, messType="info"):
                #this needs to be rewritten...
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
                self.messages += str(messageTpl)

        def login(self, username, passwd):
                foundUser = am.findUser(username)
                if foundUser:
                        if foundUser.password == bcrypt.hashpw(passwd, foundUser.password):
                                self.loggedIn = True
                                self.user = foundUser
                                self.userID = foundUser.id
                        else:
                                self.logout()
                                raise Exception("Your password appears to be wrong")
                else:
                        self.logout()
                        raise Exception("We can't find that username, are you sure it's correct?")

        def logout(self):
                self.loggedIn = False
                self.user = None
                self.userID = None
