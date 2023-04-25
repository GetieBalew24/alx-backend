#!/usr/bin/env python3
""" Get locale from request"""

from flask_babel import Babel
from flask import Flask, render_template
from flask import Flask, request


app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """ class conguration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
app.config.from_object(Config)
@app.route('/', methods=['GET'], strict_slashes=False)
def helloWorld() -> str:
    """draw 2-index.html file"""
    return render_template('2-index.html')
@babel.localeselector
def get_locale() -> str:
    """ get user locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == '__main__':
    app.run()