#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
View for authentication pages such as login
and logout.

For more information, see: https://github.com/JoshAshby/

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import baseView as bv
import templateConfig as tpl
import models.authModel as am


class indexView(bv.baseView):
        """

        """
        def HTML(self):
                page = tpl.genericTemplate(file=tpl.mainTplSet["adminIndex"])
                page.title = "Admin Home"
                return page


class userListView(bv.baseView):
        """

        """
        def HTML(self):
                page = tpl.genericTemplate(file=tpl.mainTplSet["userList"])
                page.title = "User List"
                page.userList = ""

                for user in self.data.users:
                        partial = tpl.partialTemplate(file=tpl.partialTplSet["row_list_User"])
                        partial.name = user["name"]
                        partial.notes = user["notes"]
                        partial.id = user["id"]
                        partial.perms = user["perms"]

                        partial.perms = ""
                        permList = self.data.permList
                        for perm in permList:
                                select = ""
                                if perm == user["perms"]:
                                        select = "selected"
                                partial.perms += "<option %s>%s</option>" % (select, perm)


                        page.userList += str(partial)

                return page


class newUserView(bv.baseView):
        """

        """
        def HTML(self):
                page = tpl.genericTemplate(file=tpl.mainTplSet["newUser"])
                page.title = "New User"
                page.permOptions = ""
                permList = self.data.permList
                for perm in permList:
                        page.permOptions += "<option>%s</option>" % perm

                return page


class newPostView(bv.baseView):
        """
        """
        def HTML(self):
                page = tpl.genericTemplate(file=tpl.mainTplSet["newPost"])
                page.title = "New Post"

                return page


class postListView(bv.baseView):
        """
        """
        def HTML(self):
                page = tpl.genericTemplate(file=tpl.mainTplSet["postList"])
                page.title = "Post List"
                page.postList = ""

                for post in self.data.posts:
                        partial = tpl.partialTemplate(file=tpl.partialTplSet["row_list_Post"])
                        partial.post = post.post
                        partial.author = post.author
                        partial.time = post.time
                        partial.title = post.title
                        partial.id = post.key[5:]

                        page.postList += str(partial)

                return page

