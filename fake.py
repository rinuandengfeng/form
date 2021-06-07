from app import create_app, db

from app.models.data import Data
from app.models.admin import User

app = create_app()

with app.app_context():
    db.create_all()
    user = User()
    user.username = 'admin'
    user.password = '123456'
    user.auth = 3
    user.name = '超级管理员'
    db.session.add(user)
    db.session.commit()
