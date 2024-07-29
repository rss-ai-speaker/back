from datetime import datetime
from typing import List, Optional

import feedparser
from flask_sqlalchemy import SQLAlchemy

from app.models import RSS, Content


class RssService:
    rss_s: Optional[List[RSS]]

    def __init__(self, db: SQLAlchemy, rss_s=None):
        self.db = db
        self.rss_s = rss_s

    def parse_rss(self, rss_link: str) -> List[RSS]:
        news_feed = feedparser.parse(rss_link)

        self.rss_s = self.db.session.execute(
            self.db.select(RSS).filter_by(link=rss_link)).all()
        if self.rss_s:
            return [rss[0] for rss in self.rss_s]

        self.rss_s = [RSS(link=rss_link, id=content.link, title=content.title,
                          content=content.content[0].value) for content in news_feed.entries]

        self.db.session.add_all(self.rss_s)

        return self.rss_s

    def get_rss_content_list(self) -> List[Content]:
        contents = self.db.session.query(Content).all()
        return contents

    def get_rss_content(self, content_id: str) -> Content:
        content = self.db.session.query(
            Content).filter_by(id=content_id).first()

        return content
