from flask import Flask

application = Flask(__name__)
application.config['TEMPLATES_AUTO_RELOAD'] = True