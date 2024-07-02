#!/usr/bin/env python3
"""Flask with basic babel setup"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """The app's configuration settings."""
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Delivers the index template."""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
