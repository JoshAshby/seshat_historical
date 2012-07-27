#!/usr/bin/env python2
"""
Web App/API framework built on top of gevent
Database model for authentication and users

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

from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql.expression import desc

from datetime import datetime as dt


class PostORM(Base):
        """

        """
        __tablename__ = 'posts'

        post_id = Column(Integer, primary_key=True)
        title = Column(Text)
        post = Column(Text)
        author = Column(Text)
        time = Column(DateTime)


def newPost(title, post, author):
        post = PostORM(title=title, post=post, author=author, time=dt.now())
        dbSession.add(post)

        dbSession.commit()

def updatePost(id, title, post, author):
        post = dbSession.query(PostORM).filter_by(post_id=id).first()
        post.title = title
        post.auther = author
        post.time = dt.now()

        dbSession.commit()

def listPosts():
        posts = dbSession.query(PostORM).order_by(desc(PostORM.time)).all()
        if not posts:
                raise "No Posts"
        return posts

class RedisPostORM(object):
        """
        Baisc ORM style system for Posts which are stored in Redis as hashes.
        """
        def __init__(self):
                """
                """
                self.key = max(redisPost.keys())+1

        def listPosts(self):
                for key in redisPost.keys():
                        pass

        def newPost(self, author="", title="", post=""):
                """
                """
                redisPost.hset(self.key, "author", author)
                redisPost.hset(self.key, "title", title)
                redisPost.hset(self.key, "post", post)
                redisPost.hset(self.ey, "time", dt.now())

