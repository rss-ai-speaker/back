import google.generativeai as genai
import os


class GeminiBot:
    def __init__(self,model_name):
        super().__init__()
        genai.configure(
            api_key=os.environ['GEMINI_API_KEY'])
        model = genai.GenerativeModel(
            model_name=model_name)

        self.chat = model.start_chat()

    def send_message(self,message):
        response = self.chat.send_message(message)
        return response.text
