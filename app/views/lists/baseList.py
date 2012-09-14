#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
Base object for the creation of list based items

For more information, see: https://github.com/JoshAshby/

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import sys, os

try:
        import config as c
except:
        abspath = os.path.dirname(__file__)
        sys.path.append(abspath)
        os.chdir(abspath)
        import config as c

import seshat.framework as fw
import views.templateConfig as tc
import views.baseView as bv


class baseList(object):
        def __init__(self, blocks=[], template="", width=8):
                self.blocks = blocks
                self.template = template
                self.width = width

        def build(self):
                returnData = ""

                for block in self.blocks:
                        page = tc.partialTplSet[self.template]

                        for part in block.keys:
                                if type(block[part]) != str and block[part] != None:
                                        setattr(page, part, block[part].build())
                                else:
                                        setattr(page, part, block[part])

                        returnData += bv.baseRow(str(page), self.width, 0).build()

                return returnData
