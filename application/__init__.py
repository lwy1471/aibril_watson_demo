__version__ = '0.1'
from flask import Flask
import config


print('in application')

app = Flask(__name__)
app.config['SECRET_KEY']=config.SECRET_KEY
app.debug = True

from application.controllers.controller import api_app
app.register_blueprint(api_app)