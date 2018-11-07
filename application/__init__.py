__version__ = '0.1'
from flask import Flask
import config

print('in application')
app = Flask('run')
app.config['SECRET_KEY']=config.SECRET_KEY
print(config.SECRET_KEY)
app.debug = True
from application.controllers import controller