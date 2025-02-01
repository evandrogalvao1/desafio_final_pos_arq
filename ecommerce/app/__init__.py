from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from .routes import init_routes
        init_routes(app)
        db.create_all()  # Cria as tabelas no banco de dados

    return app