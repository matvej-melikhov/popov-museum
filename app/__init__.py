from flask import Flask, request, session
from flask_babel import Babel

application = Flask(__name__)
application.config['TEMPLATES_AUTO_RELOAD'] = True
application.config['SECRET_KEY'] = 'popov-museum-dev-key'
application.config['BABEL_DEFAULT_LOCALE'] = 'ru'
application.config['BABEL_SUPPORTED_LOCALES'] = ['ru', 'en']

def get_locale():
    if 'lang' in session:
        return session['lang']
    return request.accept_languages.best_match(['ru', 'en']) or 'ru'

babel = Babel(application, locale_selector=get_locale)
application.jinja_env.globals['get_locale'] = get_locale