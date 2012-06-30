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
appName = "Seshat"
"""
What type of a server is this going to be running as?
A fastCGI server for apache, nginx or lighttpd to work with
or a stand alone server taken care of by gevent and wsgi?
"""
serverType = "fastcgi"
#serverType = "gevent"

"""
If the above serverType is set to fastcgi then we need to make
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
sessionDB = "mysql://josh:joshmysql@localhost/test"

"""
Finally we need to define the base url for various 
things such as static assets and what not.
"""
baseURL = "http://localhost"
assetURL = "http://localhost/static"
subURL = {
        "auth": "/admin",
        "test": "/test",
        }


authRegex = "(.*)_(.*)(_)"

"""
#########################STOP EDITING#####################################
***WARNING***
Don't change these following settings unless you know what you're doing!!!
##########################################################################
"""
subURLLink = {}

if serverType is "fastcgi":
        for url in subURL:
                subURLLink.update({url: fcgiBase + subURL[url]})

urls = []

session_opts = {
        'session.cookie_expires': True,
        'session.auto': True,
        'session.type': 'ext:database',
        'session.url': sessionDB,
        'session.lock_dir': './locks',
        'session.key': 'test_key',
        'session.secret': '33DJ89SQICUP9C5KRL16WHOYTY08FA430OM3YOFVXOW2PSYN8JSVIGWLVM60RDDQHXD7PT4IUTT8E3DTOD6DVAAH002BHBRECJEC',
}
