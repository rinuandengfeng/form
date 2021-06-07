from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
cors = CORS()
migrate = Migrate()


def register_blueprints(app):
    from app.api.v1.admin import admin_bp
    from app.api.v1.list import list_bp
    from app.api.v1.login import login_bp
    from app.api.v1.download import download_bp
    from app.api.v1.Pagination import paging_bp
    from app.api.v1.Pagination import search_bp
    from app.api.v1.download import download_all_bp
    app.register_blueprint(admin_bp, url_prefix='/v1')
    app.register_blueprint(list_bp, url_prefix='/v1')
    app.register_blueprint(login_bp, url_prefix='/v1')
    app.register_blueprint(download_bp, url_prefix='/v1')
    app.register_blueprint(paging_bp,url_prefix='/v1')
    app.register_blueprint(search_bp,url_prefix='/v1')
    app.register_blueprint(download_all_bp, url_prefix='/v1')

def register_plugin(app):
    cors.init_app(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
    db.init_app(app)
    from app.models.data import Data
    from app.models.admin import User
    migrate.init_app(app, db)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.settings')
    register_blueprints(app)
    register_plugin(app)
    return app
