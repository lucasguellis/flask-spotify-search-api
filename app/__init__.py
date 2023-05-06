import os
import logging
import sys

from flask import Flask
from flask_minify import Minify


logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler(filename='logs.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


def create_app():
    # App init and config
    app = Flask(__name__)
    app.config.from_object("config")
    app.config["SECRET_KEY"] = os.urandom(24)

    # Minify para reduzir tamanho de arquivos
    Minify(app=app, html=True, js=True, cssless=True)

    # app.register_blueprint(routes_base)
    # app.register_error_handler(404, error_404)
    # app.register_error_handler(401, error_401)

    from .api.v1.routes.search import api_search_bp

    api_url = "/api/v1"

    app.register_blueprint(api_search_bp, url_prefix=api_url)

    from .routes.search import search_bp

    app.register_blueprint(search_bp)

    return app
