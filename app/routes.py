from flask import render_template, flash, redirect, request, url_for
from datetime import datetime
from app import app, db

@app.route("/", methods=['GET', 'POST'])
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
    