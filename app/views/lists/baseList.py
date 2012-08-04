#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
Base object for the creation of list based items

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
import views.baseView as bv


class baseList(object):
        def __init__(self, blocks=[], template=""):
                self.blocks = blocks
                self.template = template

        def build(self):
                returnData = ""

                for block in self.blocks:
                        page = tc.partialTplSet[self.template]

                        for part in block:
                                if type(block[part]) != str:
                                        setattr(page, part, block[part].build())
                                else:
                                        setattr(page, part, block[part])

                        returnData += bv.baseRow(str(page), 8, 0).build()

                return returnData
