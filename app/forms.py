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

class CommodityForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    entry_type =StringField('Entry Type', validators=[DataRequired()])
    Quantity = StringField('Quantity', validators=[DataRequired()])
    datein = StringField('Email', validators=[DataRequired(),Email()])
    dateout = IntegerField('WhatsApp #', validators=[DataRequired()])
    notes = StringField('Notes', validators=[])
    status = StringField('Status', validators=[DataRequired()])

    shipper_id = IntegerField('Shipper',validators=[DataRequired()])
    consignee_id = IntegerField('Consignee',validators=[DataRequired()])
    customer_id = IntegerField('Customer',validators=[DataRequired()])

    submit = SubmitField('Submit Customer')