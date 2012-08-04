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
        def __init__(self, fields=[], action="", method="POST", formClass="well form-horizontal", id="", prefix=""):
                self.fields = fields
                self.action = action
                self.formClass = formClass
                self.id = id
                self.prefix = prefix
                self.method = method


class styledForm(baseForm):
        def build(self):
                """
                name
                value
                type
                class
                label
                """
                returnData = """
                <form action="%s" method="%s" class="%s" id="%s">
                        <fieldset>
                """ % (self.action, self.method, self.formClass, self.id)

                for block in self.fields:
                        if self.prefix:
                                block["name"] = self.prefix + "_" + block["name"]

                        if block.has_key("label"):
                                returnData += """
                                <div class="control-group">
                                        <label class="control-label %s" for="%s">%s</label>
                                """ % (block["class"],
                                       block["name"],
                                       block["label"])

                        if block["type"] is not "submit" and block["type"] is not "textarea":
                                returnData += """
                                <div class="controls">
                                        <input type="%s" class="%s" id="%s" name="%s" value="%s"/>
                                </div>
                                """ % (block["type"],
                                       block["class"],
                                       block["name"],
                                       block["name"],
                                       block["value"])

                        if block["type"] == "textare":
                                returnData += """
                                <div class="controls">
                                        <textarea class="%s" id="%s" name="%s">%s</textarea>
                                </div>
                                """ % (block["class"],
                                      block["name"],
                                      block["name"],
                                      block["value"])

                        if block["type"] == "submit":
                                returnData += """
                                <div class="form-actions">
                                        <button type="submit" class="btn %s" name="%s" id="%s">%s</button>
                                </div>
                                """ % (block["class"],
                                      block["name"],
                                      block["name"],
                                      block["value"])

                        if block.has_key("label"):
                                returnData += "</div>"

                returnData += "<fieldset></form>"

                return str(returnData)

