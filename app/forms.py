from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired,NumberRange, Email


class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField ('Remember Me')
    submit = SubmitField ('Sign In')








class commodityForm(FlaskForm):
    item = StringField('itemType', validators=[DataRequired()])
    entry_type = db.Column(db.String(10), index = True)
    quantity = db.Column(db.String(10), index = True)
    datein = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    dateout = db.Column(db.DateTime, index = True)
    shipper = db.Column(db.String(60), index = True)
    consignee = db.Column(db.String(60), index = True)
    customer = db.Column(db.String(60), index = True)
    notes = db.Column(db.Text)
    user_id = db.Column(db.Integer , db.ForeignKey('user.id'))