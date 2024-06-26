from flask import Blueprint

main = Blueprint('main', __name__)

def register_routes(app):
    from app.main import routes
    app.register_blueprint(main)
