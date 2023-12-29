from flask import render_template
from app import application

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/apartment-museum")
def apartment_museum():
    return render_template("apartment_museum.html")

@application.route("/laboratory-museum")
def laboratory_museum():
    return render_template("laboratory_museum.html")

@application.route("/registration")
def registration():
    return render_template("registration.html")

@application.route("/archive")
def archive():
    return render_template("archive.html");

@application.route("/success")
def success():
    return render_template("success.html")

