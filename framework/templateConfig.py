#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
Template view/controller

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

from Cheetah.Template import Template


"""
We need to define where templates live
along with partial templates
"""
tplHome = "./htmlTemplates/"
prtTplHome = "./htmlTemplates/partials/"

"""
Finally we need to define the base url for various 
things such as static assets and what not.
"""
baseURL = "http://localhost/web/"
assetURL = "http://localhost/web/static/"

#set-o-main templates. This is really here for ease of use and so forth
mainSet = {
        "index": (tplHome + "index.tpl.html"),
}

#same as above just for partials
partialSet = {
}


#generic template class, called by all the views currently
#because nothing fancy is needed.
class genericTemplate(Template):
        pass


#just one for Partials, not that it's needed, but just as a 
#reminder that your working with a partial. same as above basically.
class partialTemplate(Template):
        pass
