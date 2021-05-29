from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.utils.error_code import AuthFailed, ParameterException


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)  # 账号
    _password = db.Column(db.String(120), nullable=False)  # 密码
    auth = db.Column(db.Integer,default=1)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "adth":self.auth
        }

    @staticmethod
    def verify(username, password):
        user = User.query.filter_by(username=username).first()
        if not user:
            raise AuthFailed()
        if not user.check_password(password):
            raise ParameterException()
        scope = 'SuperAdminScope' if user.auth == 3 else \
            'AdminScope' if user.auth == 2 or user.auth == 11 or user.auth == 12 or user.auth == 13 \
                else 'UserScope'
        return {'uid': user.username,'scope':scope}

    @property
    # 增加password属性
    def password(self):
        return self._password

    @password.setter
    # 给密码进行加密
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # 给密码解密进行比对。
    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)
