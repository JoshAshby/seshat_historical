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
Finally we need to define the base url for various 
things such as static assets and what not.
"""
baseURL = "http://localhost"
assetURL = "http://localhost/static"

levels = ["admin"]

"""
#########################STOP EDITING#####################################
***WARNING***
Don't change these following settings unless you know what you're doing!!!
##########################################################################
"""
urls = []

authRegex = re.compile("([^_\W]*)")

redisPostServer = redis.Redis("localhost", db=1)
redisSessionServer = redisPostServer
redisUserServer = redisPostServer
redisPermServer = redisPostServer
