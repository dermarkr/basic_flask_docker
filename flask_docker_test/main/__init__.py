from flask import Blueprint

main = Blueprint('main', __name__)

def register_routes(app):
    from flask_docker_test.main import routes
    app.register_blueprint(main)
