from flask import Blueprint, request

from utils.custom_logger import c_logger
from ..database import db
from app.services.gemini_api import SummarizeBot
from app.services.rss_api import RssService
from ..dtos.rss_dto import RssLinkDto

bp = Blueprint('apis', __name__, template_folder='templates')


@bp.route('/api/summarize', methods=['GET','POST'])
def summarize():
    if request.method == "GET":
        args = request.args
        id = args.to_dict().get('id')

        summarize_bot = SummarizeBot(db,rss_id=id)
        response = summarize_bot.get_summary()

        return response
    else:
        rss_service = RssService(db)
        rss_link_dto = RssLinkDto(**request.json)

        rss_contents = rss_service.parse_rss(rss_link_dto.link)

        summarize_bot = SummarizeBot(db,rss_id=rss_link_dto.link,model_name="gemini-1.5-pro")

        message = ''.join(content.content for content in rss_contents)

        summarize_bot.send_message(message)

        return rss_link_dto.link
