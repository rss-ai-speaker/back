from flask import Blueprint, request, jsonify

from ..database import db
from app.services.gemini_api import SummarizeBot
from app.services.rss_api import RssService
from ..dtos.rss_dto import RssLinkDto

bp = Blueprint('apis', __name__, template_folder='templates')


@bp.route('/', methods=['GET'])
def index():
    return "Welcome to the API"


@bp.route('/api/summarize', methods=['GET', 'POST'])
def summarize():
    if request.method == "GET":
        args = request.args
        id = args.to_dict().get('id')

        summarize_bot = SummarizeBot(db)
        response = summarize_bot.get_summary(content_id=id)

        return jsonify({'text': response})
    else:
        rss_link_dto = RssLinkDto(**request.json)
        rss_service = RssService(db)
        summarize_bot = SummarizeBot(db, model_name="gemini-1.5-pro")

        rss_contents = rss_service.parse_rss(rss_link_dto.link)
        message = ''.join(content.content for content in rss_contents)

        content = summarize_bot.get_existed_content(rss_link=rss_link_dto.link)
        if content:
            return content.id

        content_id = summarize_bot.send_message(
            rss_link=rss_link_dto.link, message=message)

        return jsonify({'id': content_id})


@bp.route('/api/list', defaults={'content_id': None}, methods=['GET'])
@bp.route('/api/list/<string:content_id>', methods=['GET'])
def content_list(content_id):
    rss_service = RssService(db)

    if content_id:
        content = rss_service.get_rss_content(content_id=content_id)
        return jsonify(content)

    contents = rss_service.get_rss_content_list()
    return jsonify(contents)
