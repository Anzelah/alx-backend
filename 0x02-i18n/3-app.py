#!/usr/bin/env python3
"""Flask babel"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Configuration class
    """
    LANGUAGES = ["en", "fr"]

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Render templates
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run()
