#!/usr/bin/env python3
"""Flask with basic babel setup"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """The app's configuration settings."""
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determines the best language to use.
    This is based on the user's preference and the list of supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Delivers the index template."""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
