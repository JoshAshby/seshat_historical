#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
base form objects to build a form from...

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
        formObjectType = "label"
        def __init__(self, text):
                """
                """
                pass

        def build(self):
                """
                """
                pass


class baseButton(object):
        formObjectType = "button"
        def __init__(self, name, value, btnClass=""):
                """
                """
                self.values = """name="%s" """ % (name)
                self.values += """value="%s" """ % (value)
                self.values += """class="btn btn-%s" """ % (btnClass) if btnClass else """class="btn" """

        def build(self):
                """
                """
                return """<button %s />"""


class baseText(object):
        formObjectType = "text"
        def __init__(self, name, value="", width=8, placeholder=""):
                """
                """
                self.values = """name="%s" """ % (name)
                self.values += """value="%s" """ % (value)
                self.values += """class="span%s" """ % (width) if width else ""
                self.values += """placeholder="%s" """ % (placeholder) if placeholder else ""

        def build(self):
                """
                """
                return """<input type="text" %s>""" % (self.values)



class basePassword(object):
        formObjectType = "text"
        def __init__(self, name, value="", width=8, placeholder=""):
                """
                """
                self.values = """name="%s" """ % (name)
                self.values += """value="%s" """ % (value)
                self.values += """class="span%s" """ % (width) if width else ""
                self.values += """placeholder="%s" """ % (placeholder) if placeholder else ""

        def build(self):
                """
                """
                return """<input type="password" %s>""" % (self.values)


class baseTextarea(object):
        formObjectType = "text"
        def __init__(self, name, value="", width=8, placeholder=""):
                """
                """
                self.values = """name="%s" """ % (name)
                self.value = value
                self.values += """class="span%s" """ % (width) if width else ""
                self.values += """placeholder="%s" """ % (placeholder) if placeholder else ""

        def build(self):
                """
                """
                return """<textarea %s>%s</textarea>""" % (self.values, self.value)


class baseSelect(object):
        formObjectType = "select"
        def __init__(self, name, value="", width=8):
                """
                """
                pass

        def build(self):
                """
                """
                pass


class baseCheckbox(object):
        formObjectType = "boolean"
        def __init__(self, name, value=""):
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
        formObjectType = "button"
        def __init__(self, name, value):
                """
                """
                self.values = """name="%s" """ % (name)
                self.values += """value="%s" """ % (value)
                self.values += """class="btn btn-primary" """

        def build(self):
                """
                """
                return """<input type="submit" %s />""" % self.values
