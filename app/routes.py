from app import app
from flask import render_template

from app.models import Commodity

@app.route('/')
def index():
    return render_template('table.html', title='Wholesale Imports and Exports')


@app.route('/api/data')
def data():
    return {'data': [Commodity.to_dict() for Commodity in Commodity.query]}

