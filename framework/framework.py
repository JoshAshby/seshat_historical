#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
Main framework app

For more information, see: https://github.com/JoshAshby/

**WARNING**
Make sure you look through and change things in config.py
before running this file, to be sure it runs the way you want it to

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

import gevent
if serverType is "fastcgi":
	from gevent_fastcgi.server import WSGIServer
else:
	from gevent.pywsgi import WSGIServer
import signal
from beaker.middleware import SessionMiddleware


def app(env, start_response):
	"""
	WSGI app and controller

	Start off by looking through the dict of url's for a matched
	regex. If one is found, then build a dict of members, which
	includes matched groups in the regex, and query strings.

	After the dict of members is built, pass it along with the
	env to the class which is paired with the matched regex url.
	
	Finally, call the proper method in the class, send the headers
	and start streaming data as it's available.

	If the class provides a cookie/session data, then because of the way
	this all works, at the moment data can not be streammed. As a result
	it's all added together, then returned rather than sent out in chunks.
	"""
	global urls
	for url in urls:
		if serverType is "fastcgi":
			matched = url["regex"].match(env["REQUEST_URI"][len(fcgiBase):].split("?")[0])
		else:
			matched = url["regex"].match(env["PATH_INFO"])
		if matched:
			members = {}

			matchedItems = matched.groups()
			for item in range(len(matchedItems)):
				members.update({item: matchedItems[item]})
			
			query = env["QUERY_STRING"].split("&")

			for item in query:
				if item:
					parts = item.split("=")
					members.update({parts[0]: parts[1]})

			newHTTPObject = url["object"](env, members)

			routes = {
				"GET": newHTTPObject.GET(),
				"POST": newHTTPObject.POST(),
				"PUT": newHTTPObject.PUT(),
				"DELETE": newHTTPObject.DELETE()
				}

			status, headers = newHTTPObject.response()
			hasSession = url["session"]

			if hasSession:
				content = ''
				for data in routes[env["REQUEST_METHOD"]]:
					if data is not StopIteration:
						content += data
					else:
						break

				env["beaker.session"] = newHTTPObject.saveCookieJar()

				start_response(status, headers)

				yield content

			else:
				start_response(status, headers)

				for data in routes[env["REQUEST_METHOD"]]:
					if data is not StopIteration:
						yield data
					else:
						break
			break


def main():
	"""
	Server

	Starts the server and takes care of all that messy stuff.
	"""
	gevent.signal(signal.SIGQUIT, gevent.shutdown)
	global port
	global address
	if port and type(port) is str:
		port = int(port)
	if not address:
		address = "127.0.0.1"
	try:
		server = WSGIServer((address, port), SessionMiddleware(app, session_opts))

		if serverType is "fastcgi":
			print ("Now serving py as a fastcgi server at %s:%i" % (address, port))
		else:
			print ("Now serving py at %s:%i" % (address, port))
		print "Press Ctrl+c or send SIGQUIT to stop"

		print "\r\nHeres some fancy URLs also:\n\r"

		print "  Url : Class Name"
		print "  -------------------------"
		for url in urls:
			print ("  %s : %s" % (url['url'], url["object"].__name__))
		
		if serverType is "fastcgi":
			print "\r\n\r\nNo logging of requests done here."
			print "Check your server logs instead."
		else:
			print "\r\n\r\nNow logging requests:"
			print "  Remote IP - - [YYYY-MM-DD HH:MM:SS] \"METHOD url HTTP/version\" Status code Something Request timing"
			print "------------------------------------------------------------------------------------------------------"

		server.serve_forever()
	except KeyboardInterrupt:
		gevent.shutdown
