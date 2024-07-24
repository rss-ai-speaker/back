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

        summarize_bot = SummarizeBot(db)
        response = summarize_bot.get_summary(content_id=id)

        return response
    else:
        rss_link_dto = RssLinkDto(**request.json)
        rss_service = RssService(db)
        summarize_bot = SummarizeBot(db,model_name="gemini-1.5-pro")

        rss_contents = rss_service.parse_rss(rss_link_dto.link)
        message = ''.join(content.content for content in rss_contents)

        content_id = summarize_bot.send_message(rss_link=rss_link_dto.link, message=message)

        return content_id
