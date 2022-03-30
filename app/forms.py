from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email

class CustomerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name =StringField('Last Name', validators=[DataRequired()])
    company_name = StringField('Company Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    whatsapp = IntegerField('WhatsApp #', validators=[DataRequired()])
    submit = SubmitField('Submit Customer')