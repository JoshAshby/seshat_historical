#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
View for the main index page

For more information, see: https://github.com/JoshAshby/

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import baseView as bv
import templateConfig as tpl

class indexView(bv.baseView):
        def HTML(self):
                page = tpl.genericTemplate(file=tpl.mainTplSet["index"])
                page.title = "Home"
                page.topNews = ""
                page.posts = ""
                for post in self.data.posts:
                        partial = tpl.partialTemplate(file=tpl.partialTplSet["post_index"])
                        partial.title = post.title
                        partial.author = post.author
                        partial.time = post.time
                        partial.post = post.post

                        page.posts += str(partial)
                return page
