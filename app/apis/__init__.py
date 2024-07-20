from flask import Blueprint, request, current_app

from ..database import db
from app.dtos.summarize import RssDto
from app.services.gemini_api import SummarizeBot
from app.services.rss_api import RssService

bp = Blueprint('apis', __name__, template_folder='templates')


@bp.route('/api/summarize', methods=['GET'])
def summarize():
    # request_data: RssDto = RssDto(**request.json)

    rss_service = RssService(db)
    rss_contents = rss_service.parse_rss("1")

    summarize_bot = SummarizeBot(model_name="gemini-1.5-pro")

    contents = [content.content for content in rss_contents]
    message = ' '.join(content for content in contents)

    response = summarize_bot.send_message(message)

    print(response)

    return response.text


