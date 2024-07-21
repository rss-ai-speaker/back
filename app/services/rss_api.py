from datetime import datetime
from typing import List

import feedparser
from flask_sqlalchemy import SQLAlchemy

from app.models import RSS


class RssService:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def parse_rss(self, rss_link:str) -> List[RSS]:
        news_feed = feedparser.parse(rss_link)

        contents = [RSS(id=content.link,title=content.title,content=content.content[0].value) for
                    content in news_feed.entries]

        self.db.session.add_all(contents)

        return contents

    # def push_summary(self, rss_link:str) -> str:
    #     rss = self.db.session.execute(self.db.select(RSS).filter(RSS.link == rss_link).first())
    #     rss.su
