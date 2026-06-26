from flask import render_template, request, redirect, url_for, session
from app import application

@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/apartment-museum")
def apartment_museum():
    return render_template("apartment.html")

@application.route("/laboratory-museum")
def laboratory_museum():
    return render_template("laboratory.html")

@application.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        date = request.form.get("date", "").strip()
        number = request.form.get("number", "").strip()
        email = request.form.get("email", "").strip()
        if name and date and (number or email):
            return redirect(url_for("success"))
        return redirect(url_for("failure"))
    return render_template("registration.html")

@application.route("/archive")
def archive():
    return render_template("archive.html")

@application.route("/set-lang/<lang>")
def set_lang(lang):
    if lang in ['ru', 'en']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('index'))

@application.route("/success")
def success():
    return render_template("success.html")

@application.route("/failure")
def failure():
    return render_template("failure.html")
