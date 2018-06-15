from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login
from hashlib import md5
from flask_login import UserMixin



class Athlete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    olympic_year = db.Column(db.Integer, index=True, default=datetime.utcnow().year)
    firstname = db.Column(db.String(25), index=True, nullable=False)
    surname = db.Column(db.String(25), index=True, nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.String(8), nullable=False)
    email = db.Column(db.String(30), index=True, nullable=False,unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    athlete_picture_url = db.Column(db.String(128), nullable=True)
    #athlete_sport_event = db.relationship('AthleteSportEvent', backref='athlete_sport_event', lazy='dynamic')
    result = db.relationship('Result', backref='result', lazy='dynamic')


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    olympic_year = db.Column(db.Integer, index=True,default=datetime.utcnow().year)
    country_name = db.Column(db.String(30), index=True, nullable=False)
    geolocation = db.Column(db.String(30), nullable=False)
    climate = db.Column(db.String(20), nullable=False)
    continent = db.Column(db.String(20), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    population= db.Column(db.Integer, nullable=False)
    num_of_states = db.Column(db.Integer, nullable=False)
    president = db.Column(db.String(50), nullable=False)
    athlete = db.relationship('Athlete', backref='athlete', lazy='dynamic')
    stadium = db.relationship('Stadium', backref='stadium', lazy='dynamic')
    #   olympic_year = db.relationship('OlympicYear', backref='olympic_year', lazy='dynamic')


class Sport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sport_category = db.Column(db.String(30), index=True, nullable=False)
    sport_event = db.Column(db.String(30), index=True, nullable=False)
    olympic_year = db.Column(db.Integer, index=True, default=datetime.utcnow().year)
    #athlete_sport_event = db.relationship('AthleteSportEvent', backref='athlete_sport_event', lazy='dynamic')
    # stadium_sport_event = db.relationship('StadiumSportEvent', backref='stadium_sport_event', lazy='dynamic')


class Stadium(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stadium_name = db.Column(db.String(30), index=True, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    location = db.Column(db.String(50), nullable=False)
    olympic_year = db.Column(db.Integer, index=True, default=datetime.utcnow().year)
    # stadium_picture_url = db.Column(db.String(30))
    stadium_sport_event = db.relationship('StadiumSportEvent', backref='stadium_sport_event', lazy='dynamic')


# class AthleteSportEvent(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     athlete_id = db.Column(db.Integer, db.ForeignKey('athlete.id'))
#     sport_event_id = db.Column(db.Integer,db.ForeignKey('sport_event.id'))


class StadiumSportEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stadium_id = db.Column(db.Integer, db.ForeignKey('stadium.id'), nullable=False)
    sport_event_id = db.Column(db.Integer, db.ForeignKey('sport.id'), nullable=False)


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    olympic_year = db.Column(db.Integer, index=True, default=datetime.utcnow().year)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athlete.id'), nullable=False)
    # there would be sport field
    # In REsult form
    # but that will just help determine dynamic event
    stadium_id = db.Column(db.Integer, db.ForeignKey('stadium.id'), nullable=False)
    sport_event_id = db.Column(db.Integer,db.ForeignKey('sport.id'), nullable=False)
    position = db.Column(db.Integer, index=True, nullable=False)


# class OlympicYear(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     year = db.Column(db.DateTime, index=True, default=datetime.utcnow().year)
#     participating_country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
#     # mascot = db.Column(db.String(30), unique=True)


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))
