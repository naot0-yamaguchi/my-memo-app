import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

    from .database import init_db
    init_db(app)

    with app.app_context():
        from .route import create_route
        create_route(app)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
