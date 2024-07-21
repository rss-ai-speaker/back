from flask import Blueprint, request, current_app

from ..database import db
from app.services.gemini_api import SummarizeBot
from app.services.rss_api import RssService
from ..dtos.rss_dto import RssLinkDto

bp = Blueprint('apis', __name__, template_folder='templates')


@bp.route('/api/summarize', methods=['POST'])
def summarize():
    rss_service = RssService(db)
    rss_link_dto = RssLinkDto(**request.json)

    rss_contents = rss_service.parse_rss(rss_link_dto.link)

    summarize_bot = SummarizeBot(model_name="gemini-1.5-pro")

    contents = [content.content for content in rss_contents]
    message = ' '.join(content for content in contents)

    response = summarize_bot.send_message(message)

    return response.text


