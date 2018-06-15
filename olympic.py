from app import app, db

from app.models import Admin, Athlete, Stadium, Sport, Country
from app.models import StadiumSportEvent # , AthleteSportEvent, OlympicYear

@app.shell_context_processor
def make_shell_context():
    return {'db': db,
    'Admin': Admin,
    'Athlete': Athlete,
    'Stadium': Stadium,
    'Sport': Sport,
    'Country': Country,
#    'AthleteSportEvent': AthleteSportEvent,
    'StadiumSportEvent': StadiumSportEvent,
#    'OlympicYear': OlympicYear
    }
