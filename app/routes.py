from flask import render_template, flash, redirect, request, url_for
from datetime import datetime
from app import app, db
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user
from flask_login import login_required
from app.forms import LoginForm, RegisterAthleteForm, RegisterCountryForm
from app.forms import RegisterStadiumForm, RegisterSporteventForm
from app.models import Admin, Athlete, Country, Stadium
from app.models import SportEvent, StadiumSportEvent, AthleteSportEvent
# from app.models import OlympicYear



@app.route("/", methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html",
    title="home page",
    year=datetime.now().year)

@app.route("/about")
def about():
    return render_template("about.html",
    title="about page",
    year=datetime.now().year)

@app.route("/contact")
def contact():
    return render_template("contact.html",
    title="contact page",
    year=datetime.now().year)

@app.route("/medaltable")
def result():
    return "This is the  medal table output page"


@app.route('/login', methods=['GET', 'POST'])
def adminlogin():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin is None or not admin.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('adminlogin'))
        login_user(admin, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template("login.html",
    title="Admin Login Page",
    year=datetime.now().year,
    form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin_dashboard():

    return render_template(
        'admindashboard.html',
        title='Admin Dashboard | Olympic',
        year = datetime.now().year,
        #form=form
    )

@app.route('/admin/registerathlete',methods=['GET', 'POST'])
@login_required
def register_athlete():

    form = RegisterAthleteForm()
    form.country.choices = [(c.id, c.country_name) for c in Country.query.order_by('country_name').all()]
    country = Country.query.all()
    if form.validate_on_submit():
        athlete_firstname = form.firstname.data
        athlete_surname = form.surname.data
        athlete_gender = form.gender.data
        athlete_date_of_birth = form.date_of_birth.data
        athlete_email = form.email.data
        athlete_country = form.country.data
        athlete_image = form.picture.data
        image_filename = secure_filename(athlete_image.filename)
        athlete_image.save(os.path.join(
        app.instance_path, 'photos', filename
        ))
        flash("Athlete data received successfully")
        return redirect(url_for('register_athlete'))





    return render_template("registerathlete.html",
        title='Athlete Registeration| Admin section',
        year = datetime.now().year,
        form=form
        )


@app.route('/admin/registercountry',methods=['GET', 'POST'])
@login_required
def register_country():

    form = RegisterCountryForm()

    if form.validate_on_submit():
        country_name = form.country_name.data
        country_location = form.country_geolocation.data



        flash("Country data received successfully")
        return redirect(url_for('register_country'))


    return render_template("registercountry.html",
        title='Country Registeration| Admin section',
        year = datetime.now().year,
        form=form
        )

@app.route('/admin/registerstadium', methods=['GET','POST'])
@login_required
def register_stadium():
    form = RegisterStadiumForm()
    if form.validate_on_submit():


        print("Hello")
        return redirect(url_for('register_stadium'))

    return render_template("registerstadium.html",
    title="Stadium Registeration | Admin Section",
    year = datetime.now().year,
    form=form)

@app.route('/admin/registersportevent', methods=['GET','POST'])
@login_required
def register_sport_event():
    form = RegisterSporteventForm()
    if form.validate_on_submit():


        print("Hello")
        return redirect(url_for('register_sport_event'))

    return render_template("registerevent.html",
    title="Sport Event Registeration | Admin Section",
    year = datetime.now().year,
    form=form)
