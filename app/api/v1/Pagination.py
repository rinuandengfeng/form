from flask import Blueprint, request

from app.models.data import Data
from app.utils.to_json import items_to_json

paging_bp = Blueprint('pagin_bp', __name__)
search_bp = Blueprint('search_bp',__name__)


@paging_bp.route('/admin/page', methods=['GET'])
def paging():
    info = []
    data = request.args
    num = Data.query.all()
    infos = Data.query.filter().paginate(int(data['page']), int(data['limit']))
    return {
        "code": 20000,
        "data": {
                    "items":items_to_json(infos.items),
                    "total":len(num)

        }
    }

@search_bp.route('/admin/search')
def search():
    name = request.args.get('name')
    mes = Data.query.filter_by(name = name ).all()
    return {
        "code":20000,
        "data":items_to_json(mes)
    }


