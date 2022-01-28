from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired,NumberRange, Email


class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField ('Remember Me')
    submit = SubmitField ('Sign In')