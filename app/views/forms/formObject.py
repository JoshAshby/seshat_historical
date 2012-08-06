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
                pass

        def build(self):
                """
                """
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
