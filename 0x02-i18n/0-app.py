#!/usr/bin/env python3
"""A flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Render templates
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run()
