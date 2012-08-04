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
        def __init__(self):
                self.blocks = {}

        def __setitem__(self, block, value):
                self.blocks.update({block: value})

        def build(self):
                page = tc.mainTplSet["default"]
                for block in self.blocks:
                        if type(self.blocks[block]) != str:
                                setattr(page, block, self.blocks[block].build())
                        else:
                                setattr(page, block, self.blocks[block])
                return str(page)


class noSidebarView(baseView):
        def build(self):
                page = tc.mainTplSet["noSidebar"]
                for block in self.blocks:
                        if type(self.blocks[block]) != str:
                                setattr(page, block, self.blocks[block].build())
                        else:
                                setattr(page, block, self.blocks[block])
                return str(page)


class sidebarView(baseView):
        def build(self):
                page = tc.mainTplSet["sidebar"]
                for block in self.blocks:
                        if type(self.blocks[block]) != str:
                                setattr(page, block, self.blocks[block].build())
                        else:
                                setattr(page, block, self.blocks[block])
                return str(page)


class baseRow(object):
        def __init__(self, block, width="8", offset="2"):
                self.block = block
                self.width = width
                self.offset = offset

        def build(self):
                width = "span%s" % self.width
                if self.offset: offset = " offset%s" % self.offset
                classes = width + offset
                returnData = """
                <div class="row">
                        <div class="%s">
                        %s
                        </div>
                </div>
                """ % (classes, self.block.build())

                return str(returnData)
