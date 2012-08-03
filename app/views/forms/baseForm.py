#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
base form object which provides the ability to generate a form

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

import seshat.framework as fw


"""
This should be expanded to styled with form controls
and unstyled for placment into things like dropdowns and that...
Both should just have to override build to place in the styles...
maybe formClass will be removed if thats the case...
"""
class baseForm(object):
        def __init__(self, fields=[], action="", formClass="", id="", prefix=""):
                self.fields = fields
                self.action = action
                self.formClass = formClass
                self.id = id
                self.prefix = prefix

        def __setitem__(self, value):
                self.fields.append(value)

        def build(self):
                """
                name
                value
                type
                class
                required
                label
                """
                returnData = "<form action=\"%s\" class=\"%s\" id=\"%s\">" % (self.action, self.formClass, self.id)
                for block in self.fields:
                        if self.prefix:
                                block["name"] = self.prefix + "_" + block["name"]

                        returnData += "<input type=\"%s\" class=\"%s\" id=\"%s\" value=\"%s\" name=\"%s\" />" % (block["type"], block["class"], block["name"], block["value"], block["name"])

                returnData += "</form>"

                return str(returnData)

