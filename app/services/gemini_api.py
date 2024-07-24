from typing import List

import google.generativeai as genai
import os

from app.models import Content
from utils.custom_logger import c_logger


class GeminiBot:
    def __init__(self,model_name):
        super().__init__()
        genai.configure(
            api_key=os.getenv('GEMINI_API_KEY'))
        self.model = genai.GenerativeModel(
            model_name=model_name)

    def send_message(self,message: str):
        response = self.model.generate_content(message)
        return response.text


class SummarizeBot(GeminiBot):
    def __init__(self,db,model_name='gemini-1.5-pro'):
        self.db = db
        super().__init__(model_name)

    def send_message(self,rss_link:str,message: str):
        template = "Please summarize the content of this data"\
                   ". Focus on key headlines"\
                   ", publication dates, and brief descriptions"\
                   " of the main articles. DATA:{data}".format(data=message)

        response = self.model.generate_content(template)
        content = Content(rss_link=rss_link,summary=response.text)

        return content.id

    def get_summary(self,content_id:str)->str:

        content = self.db.session.execute(self.db.select(Content).filter_by(id=content_id)).first()

        return content[0].summary
