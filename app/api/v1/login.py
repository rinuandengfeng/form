from flask import Blueprint, request, g

from app.models.admin import User
from app.utils import response
from app.utils.encryption import encrypt
from app.utils.response import response_data
from app.utils.token import get_token, auth

login_bp = Blueprint('login_bp', __name__)


@login_bp.route('/user/login', methods=['POST'])
def login():
    a = request
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    current_user = User.verify(username, password)

    if current_user:
        token = get_token(username, password)
        # 返回认证成功
        return {
            "code": 20000,
            "data": "admin_token"
        }


@login_bp.route('/user/info', methods=['GET'])
def get_info():
    # info = User.query.filter_by(id=g.user.uid).first()
    return {
        "code": 20000,
        "data": {
            "roles": ["admin"],
            "introduction": "introduction",
            "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
            # "name": info.name
            "name": "Super Admin"
        }
    }


@login_bp.route('/user/logout', methods=['POST'])
def logout():
    return response_data(response.SUCCESS)
