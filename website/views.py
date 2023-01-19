#Fisier pentru endpoint-uri
from flask import Blueprint, render_template

endpoints = Blueprint('endpoints', __name__)

@endpoints.route('/')
def home():
    return render_template("home.html")
