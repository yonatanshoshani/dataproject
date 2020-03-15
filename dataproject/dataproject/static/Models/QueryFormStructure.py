from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, DateField
from wtforms import validators, ValidationError

from wtforms.validators import DataRequired

class LoginFormStructure(FlaskForm):
    username   = StringField('User name:  ' , validators = [DataRequired("please enter your first name")])
    password   = PasswordField('Pass word:  ' , validators = [DataRequired("please enter your password")])
    submit = SubmitField('Submit')


class UserRegistrationFormStructure(FlaskForm):
    FirstName  = StringField('First name:  ' , validators = [DataRequired("please enter your first name")])
    LastName   = StringField('Last name:  ' , validators = [DataRequired("please enter your last name")])
    PhoneNum   = StringField('Phone number:  ' , validators = [DataRequired()])
    EmailAddr  = StringField('E-Mail:  ' , validators = [DataRequired()])
    username   = StringField('User name:  ' , validators = [DataRequired()])
    password   = PasswordField('Pass word:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')
