from flask import render_template
from findagardener import app, db
from findagardener.models import GardnerServiceAssociation, Service, Gardener, Region
#from findagardener.models import Category, Task

@app.route("/")
def home():
    return render_template("gardeners.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/add_service", methods=["GET", "POST"])
def add_service():
    return render_template("add_service.html")