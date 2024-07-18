import requests
from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound

from app.services.gemini_api import GeminiBot

bp = Blueprint('apis', __name__, template_folder='templates')


@bp.route('/api/chat', methods=['POST'])
def chat():
    request_data = request.get_json()
    bot = GeminiBot(model_name="gemini_pro")

    response = bot.send_message(request_data)

    print(request_data)
    return response


