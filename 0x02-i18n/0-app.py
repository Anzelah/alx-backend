#!/usr/bin/env python3
"""A flask app"""
from flask import Flask
app = Flask(__name__)


@app.route('/')



if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
