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
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker

import bcrypt

engine = create_engine(authDB)

Base = declarative_base()

Session = sessionmaker(bind=engine)
dbSession = Session()


class UserORM(Base):
        """

        """
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True)
        name = Column(String(100))
        password = Column(String(100))
        perms = Column(String(25))
        notes = Column(Text)

class PermsORM(Base):
        """
        """
        __tablename__ = "perms"

        perms_id = Column(Integer, primary_key=True)
        perm = Column(String(25))


def loginUser(user, password, session):
        """

        """
        user = dbSession.query(UserORM).filter_by(name=user).first()

        if user:
                hashedUserPasswd = user.password

                hashedPassedPasswd = bcrypt.hashpw(password, hashedUserPasswd)

                if hashedPassedPasswd == hashedUserPasswd:
                        session['login'] = True
                        session['user'] = user.name
                        return session

def logoutUser(session):
        """

        """
        session['login'] = False
        session['user'] = "Anon"
        return session

def newUser(user, passwd, perms, session, notes=""):
        """
        """
        userExists = dbSession.query(UserORM).filter_by(name=user).all()
        print userExists
        if not userExists:
                passwordHash = bcrypt.hashpw(passwd, bcrypt.gensalt())
                user = UserORM(name=user, password=passwordHash, perms=perms, notes=notes)
                dbSession.add(user)
                dbSession.commit()
        return session

def checkPerms(session, perms):
        user = dbSession.query(UserORM).filter_by(name=session["user"]).first()
        if user.perms == "GOD":
                return True
        if user.perms == perms:
                return True
        return False

def permList():
        permList = []
        perms = dbSession.query(PermsORM).all()
        for perm in perms:
                permList.append(perm.perm)
        return permList
