__version__ = '0.1'
from flask import Flask, render_template
import config


print('in application')

app = Flask(__name__)
app.config['SECRET_KEY']=config.SECRET_KEY
app.debug = True

@app.route('/')
def home():
        return render_template('home.html')
        
from application.controllers.controller import ApiContoller
app.register_blueprint(ApiContoller.api_app, url_prefix='/service')

