#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
Base object for the creation of template objects.
All templates by default have a menu bar, message area,
breakcrumbs, and a content area. Additional areas maybe added
by subclassing this template and adding support for that area.

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
import views.templateConfig as tc


class baseView(object):
        def __init__(self, data={}):
                self.data = data

        def __setitem__(self, item, value):
                self.data.update({item: value})

        def build(self):
                pass


class noSidebarView(baseView):
        def build(self):
                pass


class sidebarView(baseView):
        def build(self):
                pass
