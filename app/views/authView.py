#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
View for authentication pages such as login
and logout.

For more information, see: https://github.com/JoshAshby/

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import baseView as bv
import templateConfig as tpl
import models.authModel as am


class indexView(bv.baseView):
        """

        """
        def HTML(self):
                page = tpl.genericTemplate(file=tpl.mainTplSet["authIndex"])
                page.title = "Admin Home"
                return page


class loginView(bv.baseView):
        """

        """
        def HTML(self):
                page = tpl.genericTemplate(file=tpl.mainTplSet["login"])
                page.title = "Login"
                return page


class newUserView(bv.baseView):
        """

        """
        def HTML(self):
                page = tpl.genericTemplate(file=tpl.mainTplSet["newUser"])
                page.title = "New User"
                page.permOptions = ""
                permList = am.permList()
                for perm in permList:
                        page.permOptions += "<option>%s</option>" % perm
                return page
