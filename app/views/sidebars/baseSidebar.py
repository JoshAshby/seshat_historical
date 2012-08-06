#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
Base object for the generation of sidebars from a python set

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


class baseSidebar(object):
        def __init__(self, blocks, active=0):
                """
                {"link": "",
                "label": ""
                "class": "",
                "id": "",
                "divide": bool}
                """
                self.blocks = blocks
                self.active = active

        def build(self):
                returnData = """<ul class="nav nav-list">"""

                for link in self.blocks:
                        if not link.has_key("type"):
                                classes = ""
                                if type(link["label"]) != str:
                                        link["label"] = link["label"].build()
                                if link.has_key("id") and link["id"] == self.active: classes = "active"
                                returnData += """
                                <li class="%s">
                                        <a href="%s" class="%s" id="%s">%s</a>
                                </li>
                                """ % (classes,
                                      link["link"],
                                      link["class"] if link.has_key("class") else "",
                                      link["id"] if link.has_key("id") else "",
                                      link["label"])
                        else:
                                returnData += link["object"].build()

                        if link.has_key("divide"):
                                returnData += """<li class="divider"></li>"""

                returnData += """</ul>"""

                return returnData

