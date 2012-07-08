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

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import desc

from datetime import datetime as dt


engine = create_engine(authDB)

Base = declarative_base()

Session = sessionmaker(bind=engine)
dbSession = Session()


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

def listPosts():
        posts = dbSession.query(PostORM).order_by(desc(PostORM.time)).all()
        if not posts:
                raise "No Posts"
        return posts
