#!/usr/bin/env python3
"""Flask babel"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration class
    """
    LANGUAGES = ["en", "fr"]

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@app.route('/')
def index():
    """Render templates
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run()
