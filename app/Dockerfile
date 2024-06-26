FROM python:3.9

WORKDIR /src/

COPY ./requirements.txt /src/app/requirements.txt
RUN pip install --no-cache-dir -r /src/app/requirements.txt

COPY ./main/ app/main/  
COPY ./templates/ app/templates/
COPY ./static/ app/static/
COPY ./__init__.py app/__init__.py
COPY ./config.py app/config.py
