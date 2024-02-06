#!/usr/bin/env python3
"""Implement Flask app and makes use of babel multiple languages."""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """For indicating available languages for the Flask app."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


flask_app = Flask(__name__)
flask_app.config.from_object(Config)
babel = Babel(flask_app)


@flask_app.route("/")
def index():
    """Serves the index.html template."""
    return render_template("1-index.html")


if __name__ == "__main__":
    flask_app.run(debug=True)
