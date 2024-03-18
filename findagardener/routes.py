from flask import render_template
from findagardener import app, db
from findagardener.models import GardnerServiceAssociation, Service, Gardener, Region
#from findagardener.models import Category, Task

@app.route("/")
def home():
    return render_template("base.html")