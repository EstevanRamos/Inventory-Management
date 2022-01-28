from app import app
from flask import render_template
from forms import LoginForm

from app.models import Commodity

app.config['SECRET_KEY'] = 'd9853defe860cd4c0be6b473aeb28bbc'

@app.route('/')
def index():
    return render_template('table.html', title='Wholesale Imports and Exports')


@app.route('/api/data')
def data():
    return {'data': [Commodity.to_dict() for Commodity in Commodity.query]}

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.hml', title = 'Register', form = form)
