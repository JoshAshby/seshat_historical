#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
Base object for the creation of template objects.
All templates by default have a menu bar, message area,
breakcrumbs, and a content area. Additional areas maybe added
by subclassing this template and adding support for that area.

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
                width = "span%s" % self.width if self.width else ""
                offset = " offset%s" % self.offset if self.offset else ""
                classes = width + offset
                returnData = """
                <div class="row">
                        <div class="%s">
                        %s
                        </div>
                </div>
                """ % (classes, self.block.build() if type(self.block) is not str else self.block)

                return str(returnData)


class baseIcon(object):
        def __init__(self, icon="", label="", white=False):
                self.icon = icon
                self.label = label
                self.white = white

        def build(self):
                if self.white: self.white = "icon-white"
                else: self.white=""
                returnData = """
                <i class="icon-%s %s"></i> %s
                """ % (self.icon, self.white, self.label)

                return returnData
