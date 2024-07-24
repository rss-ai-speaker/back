from datetime import datetime
from typing import Optional
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
import uuid

from .database import db


def gen_uuid():
    return str(uuid.uuid4())

class RSS(db.Model):
    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[str] = mapped_column()

    def __init__(self, link, title, content):
        self.id = link
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        db.session.add(self)
        db.session.commit()


class Content(db.Model):
    id: Mapped[str] = mapped_column(primary_key=True)
    rss_link: Mapped[str] = mapped_column(db.ForeignKey("rss.id"), nullable=False)
    summary:Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column()

    def __init__(self,rss_link:str,summary:str,created_at:Optional[datetime]= None):
        self.id = gen_uuid()
        self.rss_link = rss_link
        self.summary = summary
        self.created_at = created_at if created_at else datetime.now()
        db.session.add(self)
        db.session.commit()

