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

#---------------------ExpandForm--------------------------#
#
#-----------------------------------------------------------------------------------#
class ExpandForm(FlaskForm):
    submit1 = SubmitField('Expand')
    name="Expand" 
    value="Expand"

#---------------------CollapseForm--------------------------#
#
#-----------------------------------------------------------------------------------#
class CollapseForm(FlaskForm):
    submit2 = SubmitField('Collapse')
    name="Collapse" 
    value="Collapse"


