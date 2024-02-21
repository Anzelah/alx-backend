#!/usr/bin/env python3
"""Flask babel"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz


class Config:
    """Configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """Return a user dictionary
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None

@app.before_request
def before_request():
    """Execute this before all other functions
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages
    """
    req_locale = request.args.get('locale')

    if req_locale and req_locale in app.config['LANGUAGES']:
        return req_locale

    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    header_locale = request.header.get('Accept-language')
    if header_locale:
        header_locale = header_locale.split(',')[0]
    if header_locale in app.config['LANGUAGES']:
        return header_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Infer the appropriate timezone
    """
    timezone = request.args.get('timezone')
    if g.user and timezone is None:
        return g.user['timezone']

    try:
        return pytz.timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']

@app.route('/')
def index():
    """Render templates
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run()
