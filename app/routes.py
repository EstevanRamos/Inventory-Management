from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('ajax_table.html', title='Ajax Table')


@app.route('/api/data')
def data():
    return {'data': [user.to_dict() for user in User.query]}

