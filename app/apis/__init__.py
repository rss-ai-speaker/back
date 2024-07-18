from flask import Blueprint, request

from app.dtos.chat import ChatDto
from app.services.gemini_api import GeminiBot

bp = Blueprint('apis', __name__, template_folder='templates')


@bp.route('/api/chat', methods=['POST'])
def chat():
    request_data: ChatDto = ChatDto(**request.json)
    bot = GeminiBot(model_name="gemini-1.5-pro")

    response = bot.send_message(request_data.message)

    return response


