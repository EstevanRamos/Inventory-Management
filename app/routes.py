from app import app
from flask import render_template, redirect, flash, request, url_for
from app.forms import CustomerForm
from app.models import Commodity, Customer , db

@app.route('/')
def index():
    return render_template('table.html', title='Wholesale Imports and Exports')


@app.route('/api/data')
def data():
    return {'data': [Commodity.to_dict() for Commodity in Commodity.query]}

@app.route('/Customer' , methods = ('GET', 'POST'))
def customer():
    form = CustomerForm()
    if form.validate_on_submit():
        new_customer = Customer()
        form.populate_obj(new_customer)
        db.session.add(new_customer)
        try:
            db.session.commit()
            flash('Customer created', 'success')
            return redirect(url_for('Customer'))
        except:
            db.session.rollback()
            flash
    return render_template('customer_form.html', title = 'Wholesale Imports and Exports', form = form)
