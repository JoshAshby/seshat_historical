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
tplHome = "./views/htmlTemplates/"
prtTplHome = "./views/htmlTemplates/partials/"

#set-o-main templates. This is really here for ease of use and so forth
mainTplSet = {
        "index": (tplHome + "index.tpl.html"),
        "authIndex": (tplHome + "authIndex.tpl.html"),
        "login": (tplHome + "login.tpl.html"),
        "newUser": (tplHome + "newUser.tpl.html"),
}

#same as above just for partials
partialTplSet = {
}

#generic template class, called by all the views currently
#because nothing fancy is needed.
class genericTemplate(Template):
        baseURL = baseURL
        assetURL = assetURL
        subURL = subURL
        navTitle = appName
        nav = " "
        crumbs = " "
        footerLinks = " "
        messages = " "


#just one for Partials, not that it's needed, but just as a 
#reminder that your working with a partial. same as above basically.
class partialTemplate(Template):
        pass
