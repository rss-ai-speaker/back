from datetime import datetime
from typing import Optional
import sqlalchemy as sa
from .database import db


class RSS(db.Model):
    id = db.Column(db.String(120),unique=True, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self,id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        db.session.add(self)
        db.session.commit()


# class Content(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     rss_id = db.Column(db.Integer, db.ForeignKey("rss.id"), nullable=False)
#     summary = db.Column(db.String(120), nullable=False)
#     created_at = db.Column(db.DateTime, nullable=False)
#
#     def __init__(self,rss_id:int,summary:str,created_at:Optional[datetime]=None):
#         self.rss_id = rss_id
#         self.summary = summary
#         self.created_at = created_at if created_at else datetime.now()
#         db.session.add(self)
#         db.session.commit()

