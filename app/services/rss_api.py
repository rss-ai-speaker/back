from datetime import datetime
from typing import List

import feedparser
from flask_sqlalchemy import SQLAlchemy

from app.models import RSS, Content


class RssService:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def parse_rss(self, rss_link:str) -> List[Content]:
        news_feed = feedparser.parse(rss_link)

        contents = [Content(id=content.id,title=content.title,content=content.content[0].value) for content in
                    news_feed.entries]

        self.db.session.add_all(contents)

        return contents
