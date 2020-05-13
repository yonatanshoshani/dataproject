
from dataproject import app
from dataproject.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines

from datetime import datetime
 
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
from os import path
 
from flask   import Flask, render_template, flash, request,redirect
from wtforms import Form, BooleanField, StringField, PasswordField, validators,SubmitField
from wtforms import TextField, TextAreaField, SelectField, DateField
from wtforms import ValidationError

from dataproject.Models.QueryFormStructure import QueryFormStructure
## The import 'QueryFormStructure' form used to select parameters to display the graph on the data query page.
from dataproject.Models.QueryFormStructure import LoginFormStructure
from dataproject.Models.QueryFormStructure import UserRegistrationFormStructure
 ##Import the forms that the user fills in order to register or login to the website
from dataproject.Models.Fos import ExpandForm
from dataproject.Models.Fos import CollapseForm
 ##Import the completed forms to expand or Coolapse the databases.
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)
 


from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
 
 
 
db_Functions = create_LocalDatabaseServiceRoutines()
 
app.config['SECRET_KEY'] = 'All You Need Is Love Ta ta ta ta ta'
 
## The route to the home page
@app.route('/')
@app.route('/home')
def home():
    """Renders the 'home' page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

 ## The route to the 'contact' page
@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Here you have my contact information-'
    )

 ## The route to the 'PhotoAlbum' page
@app.route('/PhotoAlbum')
def PhotoAlbum():
    """Renders the PhotoAlbum page."""
    return render_template(
        'PhotoAlbum.html',
        title='Gallery',
        year=datetime.now().year,
    )
 
## The route to the 'about' page
@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
       
    )
 
## The route to the 'datamodel' page
@app.route('/datamodel')
def datamodel():
    """Renders the about page."""
    return render_template(
        'datamodel.html',
        title='Data page',
        year=datetime.now().year,
        message='Your application data page.'
    )

## The route to the register page
@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)
    # if the user presses submit
    if (request.method == 'POST' and form.validate()):
        #check if the user exist in the csv
        if (not db_Functions.IsUserExist(form.username.data)):
            # add a new user to the system
            db_Functions.AddNewUser(form)
            db_table = ""
 
            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # shows an approval message
        else:
            # shows an error message
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)
 
    return render_template(
        'register.html',
        form=form,
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )

## The route to the 'login' page
@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)
    # if the user presses submit
    if (request.method == 'POST' and form.validate()):
        # check if the login is good
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            # sends the user to the data query page
            return redirect ('DataQuery')
        else:
            #shows an error message
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html',
        form=form,
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )
 
# route to the data base 1 page
@app.route('/data/database1' , methods = ['GET' , 'POST'])
def database1():
    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    #reads the csv and converts it to data frame
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\data\Corona.csv'))
    raw_data_table = ''
    #if the user presses submit
    if request.method == 'POST':
        #if the user clicks on expand the data base will now be shown on the page
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        #if the user clicks on collapse the data base will be removed
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

## The route to the 'DataQuery' page
@app.route('/DataQuery',methods = ['GET' , 'POST'])
def DataQuery():
    ## sets the start date and the end date for the data query form.
    form = QueryFormStructure(enddate= pd.Timestamp("2016-03-23"),startdate=pd.Timestamp("2014-08-29"))
    ## shows an image until the graph is shown
    chart = "https://ichef.bbci.co.uk/news/1024/branded_news/8859/production/_108550943_ebolaepa1.jpg"
    ## reads the file and converts it to data frame
    df = pd.read_csv(path.join(path.dirname(__file__), "static/data/ebola.csv"))
    # isolates the 'country' column in the dataframe.
    s = set(df['Country'])
    # creates a list with all the countries.
    l=list(s)
    # sorts all the countries in alphabetical order.
    l.sort()
    # finds and deletes all duplications in the countries list.
    countrychoices= list(zip(l,l))
    # registers the user's choice of countries.
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

