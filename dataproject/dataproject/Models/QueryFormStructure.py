from datetime import datetime
 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, SelectMultipleField,RadioField
from wtforms import validators, ValidationError
from wtforms.fields.html5 import DateField
 
from wtforms.validators import DataRequired


##--------------------------LoginFormStructure--------------------------------##
## This class have the fields that are part of the Login form.
##  In this form the user enters his or her details and the server checks whether the entered information is correct according to parameters defined in the software.
##   The form contains several parameters -
##      The first is the 'username' field- the user enters the username
##      The second is the 'password' field - the user will enter his password
##      the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
## The parameters will be checked whether the entry is approved or not.
##---------------------------------------------------------------------##
class LoginFormStructure(FlaskForm):
    username   = StringField('User name:  ' , validators = [DataRequired()])
    password   = PasswordField('Pass word:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')

##------------UserRegistrationFormStructure--------------------## 
## This class have the fields of a registration form
##   This form is where the user can register himself. 
##  In order to register  to the website  the user must enter  some details -
##  1. Enter his 'first name' - The first name parameter is a requirement
##  2. Entering his 'Last name' - Last name parameter is required
##  3. Entering his 'Phone number' - The phone number parameter is a requirement
##  4. Enter His 'Email' - Email parameter is not required
##  5. Select 'User Name' - the user name selection parameter is a requirement
##  6. Choosing the User 'Password' - The password parameter is required
##   The 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
## after the user pess submit his information will be saved.
##--------------------------------------------------------------------------------##
class UserRegistrationFormStructure(FlaskForm):
    FirstName  = StringField('First name:  ' , validators = [DataRequired()])
    LastName   = StringField('Last name:  ' , validators = [DataRequired()])
    PhoneNum   = StringField('Phone number:  ' , validators = [DataRequired()])
    EmailAddress  = StringField('E-Mail:  ' , validators = [])
    username   = StringField('User name:  ' , validators = [DataRequired()])
    password   = PasswordField('Pass word:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')
 
##----------------------------QueryFormStructure------------------------##
## This class have the fields that the user can set, to have the query parameters for analysing the data
##  This form is where the user can select different parameters for the purpose of generating data and obtain a graph based on the parameters he has chosen.
## You can see four fields:
##   the  'countries'field- will be used to get the countries in order to make a graph that presents the countries he chose.
##   the  'startdate'field- will be used to let the user choose the start date that will be show in the graph.
##   the  'enddate'field- will be used to let the user choose the end date date that will be show in the graph.
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
##-------------------------------------------------------------------------##
class QueryFormStructure(FlaskForm):
    countries = SelectMultipleField('Select Countries:', validators = [DataRequired])
    startdate= DateField('Start Date:',format='%y-%m-%d' , validators = [DataRequired])
    enddate= DateField('End Date:',format='%Y-%m-%d' , validators = [DataRequired])
    submit = SubmitField('Submit')

