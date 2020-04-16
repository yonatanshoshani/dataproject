from datetime import datetime
from flask import render_template
from dataproject import app
from dataproject.static.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines
from dataproject.static.Models.QueryFormStructure import QueryFormStructure
 
 
from datetime import datetime
from flask import render_template, redirect, request
 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
import json
import requests
 
import io
import base64
 
from os import path
 
from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError
 
from dataproject.static.Models.QueryFormStructure import LoginFormStructure
from dataproject.static.Models.QueryFormStructure import UserRegistrationFormStructure
 
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)
 
from dataproject.static.Models.Forms import ExpandForm
from dataproject.static.Models.Forms import CollapseForm
 
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
 
 
db_Functions = create_LocalDatabaseServiceRoutines()
 
app.config['SECRET_KEY'] = 'All You Need Is Love Ta ta ta ta ta'
 
 
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
 
@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Here you have my contact information-'
    )
@app.route('/PhotoAlbum')
def PhotoAlbum():
    """Renders the PhotoAlbum page."""
    return render_template(
        'PhotoAlbum.html',
        title='Gallery',
        year=datetime.now().year,
    )
 
@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
       
    )
 
@app.route('/datamodel')
def datamodel():
    """Renders the about page."""
    return render_template(
        'datamodel.html',
        title='Data page',
        year=datetime.now().year,
        message='Your application data page.'
    )
@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)
 
    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""
 
            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)
 
    return render_template(
        'register.html',
        form=form,
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )
 
@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)
 
    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html',
        form=form,
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )
 
@app.route('/data/database1' , methods = ['GET' , 'POST'])
def database1():
    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\data\Corona.csv'))
    raw_data_table = ''
 
    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''
 
   
 
    return render_template(
        'database1.html',
        title='Data 1',
        year=datetime.now().year,
        message='My Data 1 page.',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )
 
 
@app.route('/data/database2' , methods = ['GET' , 'POST'])
def database2():
    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\data\ebola.csv'))
    raw_data_table = ''
 
    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''
 
   
 
    return render_template(
        'database2.html',
        title='Data 2',
        year=datetime.now().year,
        message='My Data 2 page.',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )
@app.route('/DataQuery',methods = ['GET' , 'POST'])
def DataQuery():
    form = QueryFormStructure()
    chart = ""
 
    df = pd.read_csv(path.join(path.dirname(__file__), "static/data/ebola.csv"))
    s = set(df['Country'])
    l=list(s)
    countrychoices= list(zip(l,l))
    form.countries.choices=countrychoices
    if request.method == 'POST':
        country_list= form.countries.data
        df['Date'] = df['Date'].astype(str)
        
        df['Date'] = df['Date'].apply(lambda x: swich_day_month(x))
        df['Date']= pd.to_datetime(df['Date'])
        df = df.loc[df["Indicator"] == 'Cumulative number of confirmed Ebola deaths']
        df3 = df.loc[df['Country'] == 'Sierra Leone']
        df3 = df3.set_index('Date')
        df3 = df3.drop(['Indicator' , 'Country' , 'value'] , 1)
        for country in country_list:
            df1 = df.loc[df['Country'] == country]
            df1 = df1.set_index('Date')
            df1 = df1.sort_index()
            df1=df1.drop(['Indicator' , 'Country'] , 1)
            df3[country] = df1['value']
        df3 = df3.fillna(value=0)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        df3.plot(ax=ax)
        chart = plot_to_img(fig)
 
 
    return render_template(
        'DataQuery.html',
        title='DataQuery',
        form=form,
        chart=chart,
        year=datetime.now().year
       
 
    )
 
def plot_to_img(fig):
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String

def swich_day_month(s):
            l = s.split('/')
            return(l[1] + '/' + l[0] + '/' + l[2])

