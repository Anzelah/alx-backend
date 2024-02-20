#!/usr/bin/env python3
"""Flask babel"""

from flask import Flask
from flask_babel import Babel


class Config:
    """Configuration class
    """
    LANGUAGES = ["en", "fr"]

app = Flask(__name__)
app.config.from_pyfile('mysettings.cfg')

babel = Babel(app)
babel.init_app(app)
app.config['LANGUAGES'] = Config.LANGUAGES



if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
