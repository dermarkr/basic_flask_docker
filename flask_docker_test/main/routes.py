from flask import render_template
from flask import current_app as app
from flask_docker_test.main import main

@main.route('/')
def index():
    return render_template('index.html')