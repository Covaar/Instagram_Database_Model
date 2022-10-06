import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    username=Column(String(20), nullable=False, unique=True)
    firstname=Column(String(20), nullable=False)
    lastname=Column(String(20), nullable=False)
    email=Column(String(50), nullable=False, unique=True)
    password=Column(String(10), nullable=False)
    created_at=Column(DateTime(), default=datetime.now())
    follower=relationship('Follower',backref='User')
    post=relationship('Post',backref='User')
    comment=relationship('Comment',backref='User')
    
class Follower(Base):
    __tablename__='followers'
    id = Column(Integer, primary_key=True)
    user_from_id=Column(Integer, ForeignKey('users.id'), nullable=False)
    user_to_id=Column(Integer, ForeignKey('users.id'), nullable=False)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('users.id'), nullable=False)
    media=relationship('Media',backref='Post', uselist=False)
    comment=relationship('Comment',backref='Post', uselist=False)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type=Column(String(50), nullable=False)
    url=Column(String(50), nullable=False)
    post_id= Column(Integer, ForeignKey('posts.id'), nullable=False)
    
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text=Column(String(120), nullable=False)
    author_id=Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id=Column(Integer, ForeignKey('posts.id'), nullable=False)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')