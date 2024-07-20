from typing import List

import google.generativeai as genai
import os


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
    def __init__(self,model_name):
        super().__init__(model_name)

    def send_message(self,message: str):
        template = "Please summarize the content of this data"\
                   ". Focus on key headlines"\
                   ", publication dates, and brief descriptions"\
                   " of the main articles. DATA:{data}".format(data=message)

        response = self.model.generate_content(template)
        return response

