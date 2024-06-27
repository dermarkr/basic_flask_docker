FROM python:3.9

WORKDIR /src/

COPY ./requirements.txt /src/flask_docker_test/requirements.txt
RUN pip install --no-cache-dir -r /src/flask_docker_test/requirements.txt

COPY ./main/ flask_docker_test/main/  
COPY ./templates/ flask_docker_test/templates/
COPY ./static/ flask_docker_test/static/
COPY ./__init__.py flask_docker_test/__init__.py
COPY ./config.py flask_docker_test/config.py
COPY ./gunicorn.conf.py /src/gunicorn.conf.py