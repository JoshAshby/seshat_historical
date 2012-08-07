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
                type (o if dbField)
                dbField (o if type)
                value (o)
                label (o)
                width (o)
                """
                returnData = """
                <form action="%s" method="%s" class="span%s">
                        <fieldset>
                """ % (self.action, self.method, self.width)

                for block in self.fields:
                        width = block["width"] if block.has_key("width") else self.width
                        if block.has_key("formObjectType"):
                                field = getattr(fo, "base" + block["type"].title())

                                if field["formObjectType"] is "button":
                                        field = field(block["name"], block["value"])

                                if field["formObjectype"] is "text":
                                        if block.has_key("placeholder"):
                                                field = field(block["name"], block["value"], width, block["placeholder"])
                                        else:
                                                field = field(block["name"], block["value"], width)

                        else:
                                field = getattr(fo, "baseText")(block["name"], block["value"], width)

                returnData += """
                        <fieldset>
                </form>
                """

                return str(returnData)


class baseControlGroup(object):
        def __init__(self, block):
                """
                """
                pass

        def build(self):
                """
                """
                pass


class baseControl(object):
        def __init__(self, block):
                """
                """
                pass

        def build(self):
                """
                """
                pass


class baseLabel(object):
        def __init__(self, text):
                """
                """
                pass

        def build(self):
                """
                """
                pass


class baseButton(object):
        def __init__(self, name, value, btnClass=""):
                """
                """
                self.btnClass = ("btn-" + btnClass) if btnClass else ""
                self.name = name
                self.value = value
                pass

        def build(self):
                """
                """
                returnData = """
                <button name="%s" value="%s" class="%s">
                """ % (self.name, self.value, self.btnClass)
                pass


class baseText(object):
        def __init__(self, name, value="", width=8, placeholder=""):
                """
                """
                pass

        def build(self):
                """
                """
                pass



class basePassword(object):
        def __init__(self, name, value="", width=8, placeholder=""):
                """
                """
                pass

        def build(self):
                """
                """
                pass


class baseTextarea(object):
        def __init__(self, name, value="", width=8, placeholder=""):
                """
                """
                pass

        def build(self):
                """
                """
                pass


class baseSelect(object):
        def __init__(self, name, options, width=8):
                """
                """
                pass

        def build(self):
                """
                """
                pass


class baseCheckbox(object):
        def __init__(self, name):
                """
                """
                pass

        def build(self):
                """
                """
                pass


class baseFormAction(object):
        def __init__(self, blocks):
                """
                """
                pass

        def build(self):
                """
                """
                pass


class baseSubmit(object):
        def __init__(self, name, value):
                """
                """
                pass

        def build(self):
                """
                """
                pass
