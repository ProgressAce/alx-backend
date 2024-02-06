#!/usr/bin/env python3
"""Implementing a basic Flask application."""

from flask import Flask, render_template

flask_app = Flask(__name__)


@flask_app.route("/")
def index():
    """Serves the index.html template."""
    return render_template("0-index.html")


if __name__ == "__main__":
    flask_app.run(debug=True)
