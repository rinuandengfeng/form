from flask import Blueprint, request

from app.models.data import Data
from app.utils.info_query import info_query
from app.utils.token import auth

list_bp = Blueprint("list_bp", __name__)


@list_bp.route('/admin/list', methods=['GET'])
def test():
    # name = request.args.get('name')
    # info = Data.query.filter_by(name='张三').first()
    # info = Data.to_json(info)
    return {
        "code": 20000,
        "data": info_query()
    }
