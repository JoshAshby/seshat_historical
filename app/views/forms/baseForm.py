#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
base form object which provides the ability to generate a form based off
of either a JSON object, or a python set.

Arrays are treated as selects, numbers as spinners,
and text as input[type="text"]

type can be changed by passing to each field what it is.

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
import util.frameworkUtil as fwUtil


class baseForm(object):
        def __init__(self, data={}):
                pass

        def build(self):
                pass

