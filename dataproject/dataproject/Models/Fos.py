from datetime import datetime
#-------------------WTF-------------#
# WT Forms is intended to provide the interactive user interface for the user. 
# The WTF is a built-in module of the flask which provides an alternative way of designing forms .
#-----------------------------------------#
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, DateField
from wtforms import validators, ValidationError

from wtforms.validators import DataRequired
from wtforms.validators import InputRequired
# all All of the above are Imports to make the forms possible to make##

#---------------------ExpandForm--------------------------#
# converts the first submit option to expand
#-----------------------------------------------------------------------------------#
class ExpandForm(FlaskForm):
    submit1 = SubmitField('Expand')
    name="Expand" 
    value="Expand"

#---------------------CollapseForm--------------------------#
#converts the second submit option to collapse
#-----------------------------------------------------------------------------------#
class CollapseForm(FlaskForm):
    submit2 = SubmitField('Collapse')
    name="Collapse" 
    value="Collapse"


