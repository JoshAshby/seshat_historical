#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
base form object which provides the ability to generate a form

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

import seshat.framework as fw
import views.forms.formObject as fo


class baseForm(object):
        def __init__(self, fields=[], action="", method="POST", width=8):
                self.fields = fields
                self.action = action
                self.method = method
                self.width = width

        def build(self):
                """
                name
                type (o - reverts to text input if none)
                value (o)
                label (o)
                width (o)
                """
                returnData = """
                <form action="%s" method="%s" class="form span%s" style="padding-right: 10px; margin-right:10px">
                        <fieldset>
                """ % (self.action, self.method, self.width)

                for block in self.fields:
                        width = block["width"] if block.has_key("width") else self.width
                        if not block.has_key("value"): block["value"] = ""

                        if block.has_key("type"):
                                field = getattr(fo, "base" + block["type"].title())

                                if field.formObjectType is "button":
                                        field = field(block["name"], block["value"])

                                if field.formObjectType is "text":
                                        if block.has_key("placeholder"):
                                                field = field(block["name"], block["value"], width, block["placeholder"])
                                        else:
                                                field = field(block["name"], block["value"], width)

                                returnData += field.build()

                        else:
                                field = getattr(fo, "baseText")
                                if block.has_key("placeholder"):
                                        field = field(block["name"], block["value"], width, block["placeholder"])
                                else:
                                        field = field(block["name"], block["value"], width)

                                returnData += field.build()

                returnData += """
                        <fieldset>
                </form>
                """

                return str(returnData)
