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
        import config as c
except:
        abspath = os.path.dirname(__file__)
        sys.path.append(abspath)
        os.chdir(abspath)
        import config as c

from Cheetah.Template import Template


"""
We need to define where templates live
along with partial templates
"""
tplHome = "./views/htmlTemplates/"
prtTplHome = "./views/htmlTemplates/partials/"


#generic template class, called by all the views currently
#because nothing fancy is needed.
class genericTemplate(Template):
        Template.baseURL = c.baseURL
        Template.assetURL = c.assetURL
        Template.navTitle = c.appName
        Template.nav = " "
        Template.crumbs = " "
        Template.footerLinks = " "
        Template.messages = " "
        Template.session = c.session


#just one for Partials, not that it's needed, but just as a 
#reminder that your working with a partial. same as above basically.
class partialTemplate(Template):
        Template.baseURL = c.baseURL
        Template.assetURL = c.assetURL
        Template.session = c.session


#set-o-main templates. This is really here for ease of use and so forth
mainTplSet = {
        "sidebar": genericTemplate(file=(tplHome + "sidebar.tpl.html")),
        "noSidebar": genericTemplate(file=(tplHome + "noSidebar.tpl.html")),
        "default": genericTemplate(file=(tplHome + "blank.tpl.html")),
}

#same as above just for partials
partialTplSet = {
        "row_list_User": partialTemplate(file=(prtTplHome + "row_list_User.tpl.html")),
        "row_list_Post": partialTemplate(file=(prtTplHome + "row_list_Post.tpl.html")),
        "post_index": partialTemplate(file=(prtTplHome + "post_index.tpl.html")),
}


