# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:13:43 2022

@author: Mario
"""

from flask import Flask

from Config import config

# Routes
import Conicas

app = Flask(__name__)


def page_not_found(error):
    return "<h1>Not found page</h1>", 404


@app.route('/')
def index():
    return '<h1>Hi, I am Mario and Who are you?</h1>'


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Conicas.main, url_prefix='/')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()
