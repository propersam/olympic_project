from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import FloatField, StringField, PasswordField, BooleanField, TextAreaField, SubmitField, DateField
from wtforms import SelectField, IntegerField, RadioField, HiddenField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import Admin, Country, Stadium, Athlete


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class RegisterAthleteForm(FlaskForm):
    formname = HiddenField('formname') # csrf into database
    firstname = StringField('Firstname', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    date_of_birth = DateField('Birth Date', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('male', 'Male'),('female','Female')], validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    country = SelectField(coerce=int)
    picture = StringField('Url Link to Image')
    register_athlete = SubmitField('Register')

class RegisterCountryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    geolocation = StringField('Geolocation', validators=[DataRequired()])
    climate = SelectField('Climate', choices=[('humid','Humid'),('cold', 'Cold'), ('snow','Snowy'), ('heat','Too hot')], validators=[DataRequired()])
    continent = SelectField('Continent', choices=[('NA', 'North America'), ('SA', 'South America'), ('AF', 'Africa'),('EU','Europe'), ('As', 'Asia')], validators=[DataRequired()] )
    num_of_state = IntegerField('Num of state', validators=[DataRequired()])
    population = IntegerField('Population', validators=[DataRequired()])
    size = FloatField('Size', validators=[DataRequired()])
    president = StringField('Country President', validators=[DataRequired()])
    register_country = SubmitField('Register')

class RegisterStadiumForm(FlaskForm):
    stadium_name = StringField('Name', validators=[DataRequired()])
    stadium_country = SelectField(coerce=int)
    stadium_location = StringField('Location/Address', validators=[DataRequired()])
    register_stadium = SubmitField('Register')

class RegisterSporteventForm(FlaskForm):
    sport = StringField('Category', validators=[DataRequired()])
    event = StringField('Event', validators=[DataRequired()])
    register_sport = SubmitField('Register')
