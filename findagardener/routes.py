from flask import render_template, request, redirect, url_for
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
    if request.method == "POST":
        service = Service(
            service_name=request.form.get("service_name"),
            service_description=request.form.get("service_description"),
            price=request.form.get("price"))
        db.session.add(service)
        db.session.commit()
        return redirect(url_for("services"))
    return render_template("add_service.html")