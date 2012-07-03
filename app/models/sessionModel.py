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
import redis

redisServer = redis.Redis("localhost")


class session(object):
        def __init__(self, sessionId):
                pickledData = redis.get(sessionId)
                self.data = pickle.loads(pickledData)

        def commit(self):
                pickledSession = pickle.dumps(self.data)
                redis.set(self.id, pickledSession)

        def __getitem__(self, item):
                pass

        def __setitem__(self):
                pass

        def __repr__(self):
                pass

        def __str__(self):
                pass

        def status(self):
                pass

        def perms(self):
                pass

        def _history(self, hist):
                pass

        def pushHistory(self, hist):
                pass

        def getHistory(self):
                pass

        def _message(self, message):
                pass

        def getMessage(self):
                pass

        def pushMessage(self, message, type="info"):
                pass
