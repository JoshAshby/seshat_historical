#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
Config settings

For more information, see: https://github.com/JoshAshby/

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import re
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import redis


appName = "Seshat"

"""
We need to make
sure that the routing is taken care of properly. I'll describe
this setting later when I have more time.
"""
fcgiBase = ""

"""
Next up, which address and port do we want the server to bind to
this is the same for fastcgi or standalone gevent.
"""
address = "127.0.0.1"
port = 8000

"""
Next, do you want this framework to do some extra debugging?
"""
debug = True

"""
Now up are the authentication and session database strings
These are just sqlalchemy database strings so docu is around
"""
authDB = "mysql://josh:joshmysql@localhost/test"

"""
Finally we need to define the base url for various 
things such as static assets and what not.
"""
baseURL = "http://localhost"
assetURL = "http://localhost/static"
subURL = {
        "admin": "/admin",
        "auth": "/auth",
        }


authRegex = re.compile("([^_\W]*)")

"""
#########################STOP EDITING#####################################
***WARNING***
Don't change these following settings unless you know what you're doing!!!
##########################################################################
"""
urls = []

engine = create_engine(authDB)

Base = declarative_base()

Session = sessionmaker(bind=engine)
dbSession = Session()

redisSessionServer = redis.Redis("localhost", db=0)
redisPostServer = redis.Redis("localhost", db=1)
