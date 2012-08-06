#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
Base object for the generation of menus for the header

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


class baseMenu(object):
        def __init__(self, left=[], right=[], active=0):
                """
                {"link": "",
                "label": ""
                "class": "",
                "id": "",
                "divide": bool}
                """
                self.left = left
                self.right = right
                self.active = active

        def build(self):
                returnData = """<ul class="nav">"""

                for link in self.left:
                        if not link.has_key("type"):
                                classes = ""
                                if type(link["label"]) != str:
                                        link["label"] = link["label"].build()
                                if link["id"] == self.active: classes = "active"
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
                                returnData += """<li class="divider-vertical"></li>"""

                returnData += """</ul><ul class="nav pull-right">"""

                for link in self.right:
                        if not link.has_key("type"):
                                classes = ""
                                if type(link["label"]) != str:
                                        link["label"] = link["label"].build()
                                if link["id"] == self.active: classes = "active"
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
                                returnData += """<li class="divider-vertical"></li>"""

                returnData += """</ul>"""

                return returnData


class baseDropdown(object):
        def __init__(self, blocks=[], label=""):
                self.blocks = blocks
                self.label = label

        def build(self):
                if type(self.label) != str:
                        self.label = self.label.build()
                returnData = """
                <li class="dropdown">
                        <a href="#"
                                class="dropdown-toggle"
                                data-toggle="dropdown">
                                %s
                                <b class="caret"></b>
                        </a>
                        <ul class="dropdown-menu">
                """ % self.label

                for block in self.blocks:
                        if not block.has_key("type"):
                                classes = ""
                                if type(block["label"]) != str:
                                        block["label"] = block["label"].build()

                                returnData += """
                                <li class="%s">
                                        <a href="%s" class="%s" id="%s">%s</a>
                                </li>
                                """ % (classes,
                                      block["link"],
                                      block["class"] if block.has_key("class") else "",
                                      block["id"] if block.has_key("id") else "",
                                      block["label"])

                        else:
                                returnData += block["object"].build()


                returnData += """
                        </ul>
                </li>
                """

                return returnData
