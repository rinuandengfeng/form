from flask import Blueprint, request

from app.models.data import Data
from app.utils.info_query import info_query
from app.utils.to_json import items_to_json
from app.utils.token import auth

list_bp = Blueprint("list_bp", __name__)


@list_bp.route('/admin/list', methods=['GET'])
# def list():
#     # name = request.args.get('name')
#     # info = Data.query.filter_by(name='张三').first()
#     # info = Data.to_json(info)
#     return {
#         "code": 20000,
#         "data": info_query()
#     }
def paging():
    info = []
    data = request.args
    num = Data.query.all()
    infos = Data.query.filter().paginate(int(data['page']), int(data['limit']))
    return {
        "code": 20000,
        "data": {
            "items": items_to_json(infos.items),
            "total": len(num)
        }
        }
