from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login
from hashlib import md5
from flask_login import UserMixin



class Athlete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(25), index=True)
    surname = db.Column(db.String(25), index=True)
    date_of_birth = db.Column(db.DateTime)
    gender = db.Column(db.String(8))
    email = db.Column(db.String(30), index=True, unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    # athlete_picture_url = db.Column(db.String(50))
    athlete_sport_event = db.relationship('AthleteSportEvent', backref='athlete_sport_event', lazy='dynamic')
    result = db.relationship('Result', backref='result', lazy='dynamic')


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(30), index=True)
    geolocation = db.Column(db.String(30))
    climate = db.Column(db.String(20))
    continent = db.Column(db.String(20))
    size = db.Column(db.Integer)
    population= db.Column(db.Integer)
    num_of_states = db.Column(db.Integer)
    athlete = db.relationship('Athlete', backref='athlete', lazy='dynamic')
    olympic_year = db.relationship('OlympicYear', backref='olympic_year', lazy='dynamic')


class SportEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sport_event = db.Column(db.String(30), index=True)
    #athlete_sport_event = db.relationship('AthleteSportEvent', backref='athlete_sport_event', lazy='dynamic')
    stadium_sport_event = db.relationship('StadiumSportEvent', backref='stadium_sport_event', lazy='dynamic')


class Stadium(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stadium_name = db.Column(db.String(30), index=True)
    location = db.Column(db.String(50))
    # stadium_picture_url = db.Column(db.String(30))
    stadium_sport_event = db.relationship('StadiumSportEvent', backref='stadium_registered_event', lazy='dynamic')


class AthleteSportEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athlete.id'))
    sport_event_id = db.Column(db.Integer,db.ForeignKey('sport_event.id'))


class StadiumSportEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stadium_id = db.Column(db.Integer, db.ForeignKey('stadium.id'))
    sport_event_id = db.Column(db.Integer, db.ForeignKey('sport_event.id'))


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athlete.id'))
    medal_won = db.Column(db.String(20))


class OlympicYear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.DateTime, index=True, default=datetime.now().year)
    participating_country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    # mascot = db.Column(db.String(30), unique=True)


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))