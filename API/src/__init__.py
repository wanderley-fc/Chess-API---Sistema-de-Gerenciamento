from flask import Flask
from flask_restful import Api
import json  
from src.routes.endpoints import initialize_endpoints
from src.entities.database import db

def create_app() -> Flask:
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:senha@localhost:5432/chess_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    api = Api(app, prefix="/xadrez")
    initialize_endpoints(api)

    @app.after_request
    def after_request(response):
        if response.mimetype == 'application/json' and response.data:
            try:
                data = json.loads(response.get_data(as_text=True))
                response.set_data(json.dumps(data, ensure_ascii=False))
                response.headers['Content-Type'] = 'application/json; charset=utf-8'
            except:
                pass
        return response

    return app