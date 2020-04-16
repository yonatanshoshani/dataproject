from datetime import datetime
 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, SelectMultipleField,RadioField
from wtforms import validators, ValidationError
from wtforms.fields.html5 import DateField
 
from wtforms.validators import DataRequired
 
class LoginFormStructure(FlaskForm):
    username   = StringField('User name:  ' , validators = [DataRequired()])
    password   = PasswordField('Pass word:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')
 
 
class UserRegistrationFormStructure(FlaskForm):
    FirstName  = StringField('First name:  ' , validators = [DataRequired()])
    LastName   = StringField('Last name:  ' , validators = [DataRequired()])
    PhoneNum   = StringField('Phone number:  ' , validators = [DataRequired()])
    EmailAddr  = StringField('E-Mail:  ' , validators = [DataRequired()])
    username   = StringField('User name:  ' , validators = [DataRequired()])
    password   = PasswordField('Pass word:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')
 
class QueryFormStructure(FlaskForm):
    countries = SelectMultipleField('Select Countries:', validators = [DataRequired])
    startdate= DateField('Start Date:',format='%Y-%m-%d' , validators = [DataRequired])
    enddate= DateField('End Date:',format='%Y-%m-%d' , validators = [DataRequired])
    submit = SubmitField('Submit')

