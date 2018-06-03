from flask import render_template, flash, redirect, request, url_for
from datetime import datetime
from app import app, db
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user
from flask_login import login_required
from app.forms import LoginForm
from app.models import Admin



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
        return redirect(url_for('index'))
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