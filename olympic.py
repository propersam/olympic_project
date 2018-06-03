from app import app, db

from app.models import Admin, Athlete, Stadium, SportEvent, Country
from app.models import AthleteSportEvent, StadiumSportEvent, OlympicYear

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 
    'Admin': Admin,
    'Athlete': Athlete,
    'Stadium': Stadium,
    'SportEvent': SportEvent,
    'Country': Country,
    'AthleteSportEvent': AthleteSportEvent,
    'StadiumSportEvent': StadiumSportEvent,
    'OlympicYear': OlympicYear}