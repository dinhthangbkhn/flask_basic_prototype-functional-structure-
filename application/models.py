from sqlalchemy import Column, Integer, String
from application.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

class Google(Base):
    __tablename__ = 'google'
    id = Column(String(10), primary_key=True)
    title = Column(String(50))

    def __init__(self, title=None):
        self.title = title

class Yahoo(Base):
    __tablename__ = 'yahoo'
    id = Column(String(10), primary_key=True)
    title = Column(String(50))

    def __init__(self, title=None):
        self.title = title

