from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template('index.html')

@views.route("/About")
def about():
    return render_template('About.html', about_active="active")

@views.route("/Tripplan")
def tripplan():
    return render_template("tripplan.html")