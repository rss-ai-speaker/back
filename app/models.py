from datetime import datetime
from typing import Optional

from .database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.created_at = datetime.now()
        db.session.add(self)
        db.session.commit()


class RSS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    link = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)

    def __init__(self, title, link, description):
        self.title = title
        self.link = link
        self.description = description
        self.datetime = datetime.now()
        db.session.add(self)
        db.session.commit()


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    rss_id = db.Column(db.Integer, db.ForeignKey('rss.id'), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, title:str, content:str,rss_id:int,created_at:Optional[datetime]=None):
        self.title = title
        self.content = content
        self.rss_id = rss_id
        self.created_at = created_at if created_at else datetime.now()
        db.session.add(self)
        db.session.commit()

