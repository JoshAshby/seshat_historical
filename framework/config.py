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
fcgiBase = "/web"

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
#########################STOP EDITING#####################################
***WARNING***
Don't change these following settings unless you know what you're doing!!!
##########################################################################
"""
urls = []

session_opts = {
	'session.cookie_expires': False,
	'session.auto': True,
	'session.type': 'file',
	'session.data_dir': './data',
	'session.validate_key': 'abc',
	'session.encrypt_key': '123',
}
