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
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

import bcrypt

engine = create_engine('mysql://josh:joshmysql@localhost/test')

Base = declarative_base()

Session = sessionmaker(bind=engine)
dbSession = Session()


class User(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True)
        name = Column(String(100))
        password = Column(String(60))


def loginUser(user, password, session):
        user = session.query(User).filter_by(name=user).first()

        if user:
                hashedUserPasswd = user.password

                hashedPassedPasswd = bcrypt.hashpw(password, hashedUserPasswd)

                if hashedPassedPasswd == hashedUserPasswd:
                        session['login'] == True
                        return session
                else:
                        return False
        else:
                return None

def newUser(user, passwd, session):
        user = User(name=user, password=passd)
        dbSession.add(user)
        session['login'] == True
        dbSession.commit()
        return session
