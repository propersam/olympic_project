from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import FloatField, StringField, PasswordField, BooleanField, TextAreaField, SubmitField, DateField
from wtforms import SelectField, IntegerField, RadioField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import Admin, Country, Stadium, Athlete


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class RegisterAthleteForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    date_of_birth = DateField('Birth Date', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('male', 'Male'),('female','Female')], validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    country = SelectField('Athlete Country', coerce=int)
    picture = FileField('Upload Image', validators = [FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    register_athlete = SubmitField('Register')

class RegisterCountryForm(FlaskForm):
    country_name = StringField('Name', validators=[DataRequired()])
    country_geolocation = StringField('Geolocation')
    climate = SelectField('Climate', choices=[('humid','Humid'),('cold', 'Cold'), ('snow','Snowy'), ('heat','Too hot')])
    continent = SelectField('Continent', choices=[('NA', 'North America'), ('SA', 'South America'), ('AF', 'Africa'),('EU','Europe'), ('As', 'Asia')] )
    num_of_state = IntegerField('Num of state', validators=[DataRequired()])
    population = IntegerField('Population', validators=[DataRequired()])
    size = FloatField('Size', validators=[DataRequired()])
    register_country = SubmitField('Register')

class RegisterStadiumForm(FlaskForm):
    stadium_name = StringField('Name', validators=[DataRequired()])
    stadium_location = StringField('Location/Address', validators=[DataRequired()])
    register_stadium = SubmitField('Register')

class RegisterSporteventForm(FlaskForm):
    sport = StringField('Sport Category', validators=[DataRequired()])
    event = StringField('Sport Event', validators=[DataRequired()])
    register_sport = StringField('Register')
