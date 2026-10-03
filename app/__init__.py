from flask import Flask
from app.config import Config, DevelopmentConfig
from app.extensions import db, migrate, jwt


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, static_folder="static", template_folder="../templates")
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Регистрация Blueprints
    from app.controllers.web.routes import web_bp
    from app.controllers.api.routes import api_bp
    from app.controllers.api.auth import auth_api_bp

    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_api_bp)

    return app
