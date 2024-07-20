from datetime import datetime
from typing import List

import feedparser
from flask_sqlalchemy import SQLAlchemy

from app.models import RSS, Content


class RssService:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def parse_rss(self, rss_id: str)-> List[Content]:
        # rss = self.db.session.execute(self.db.select(RSS).filter(RSS.id == rss_id))
        news_feed = feedparser.parse("https://www.reddit.com/r/nextjs/comments/184dy3r/nextjs_is_hard/.rss")

        contents = [Content(title=content.title+'ss ',rss_id=1,content=content.content[0].value+'  ') for content in
                    news_feed.entries]

        self.db.session.add_all(contents)

        return contents
