Seshat:
=============
A web framework thingy using gevents pywsgi server
--------------------------------------------------
* Joshua P Ashby
* 2012
* joshuaashby@joshashby.com
* http://joshashby.com
* http://www.flickr.com/photos/joshashby/
* https://github.com/JoshAshby

Foreword:
--------------
This is always changing. If something breaks, let me know. If you want to use it, clone it, if you want to modify it: fork it. If you want me to pull a change in, send a pull request. All the basic stuff.

License:
-------------
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA.

Abstract:
-------------
A web framework providing server side session intergrationg through Beaker, sqlalchemy and mysql, along with simple and easy to use functions to get data to and from where you want and need it.

Goodies:
-----------
Every page is treated as an Object, and every page can be routed to through a regex:

        @route("/url/to/route/to")
        class page(basePage):
                ...

You can also stack route decorators to have multiple URL's route to that object:

        @route("/index")
        @route("/")
        class index(basePage):
                ...

Because routing URLs are treated as regex you can also match data with in them:

        @route("/(.*)") # use self.members[0] to access what was matched to (.*) (index 0 because it's the first matched group in the regex)

Did I mention that pages are treated as objects? This means that every object is able to respond to GET/POST/PUT/DELETE, all with one routing decorator!
Check it out:

        @route("/")
        class index(basePage):
                def GET(self):
                        return "<h1>Hello, World!</h1>"

                def POST(self):
                        return "This is a post"

Page objects also allow you to access the matched groups, and query strings from the URL through a dictionary: ``members``

        def GET(self):
                for member in self.members:
                        yield member

Wait a minute... Did I just see a `yield` used with in a GET call... Yep thats right, pages can be either a static return or become a generator through the use of `yield` Although it's important to note that if a page is decorated with the @auth decorator, it must be a static return.

Pages also allow you to access the session data through... you guessed it, `session`:

        def PUT(self):
                self.session['something'] = True

Finally lets take a look at authentication real quick. It uses the session data along with a mysql table which has passwords encrypted in bcrypt hashe to make for a basic but fairly secure for small needs authentication system.

Libraries used:
----------------------
Warning: Incomplete as of now... Just listing what comes to mind.

* Beaker
* sqlalchemy
* gevent
* gevent-fastcgi
* cheetah (if using included base templates)
 - also includes some Twitter bootstrap stuff to give you an idea of what you can do
* re
