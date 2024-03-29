from flask import render_template, request, redirect, url_for
from findagardener import app, db
from findagardener.models import GardnerServiceAssociation, Service, Gardener, Region
#from findagardener.models import Category, Task

@app.route("/")
def home():
    return render_template("gardeners.html")


@app.route("/services")
def services():
    services = list(Service.query.order_by(Service.service_name).all())
    return render_template("services.html", services=services)


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


@app.route("/edit_service/<int:service_id>", methods=["GET", "POST"])
def edit_service(service_id):
    service = Service.query.get_or_404(service_id)
    if request.method == "POST":
        service.service_name = request.form.get("service_name")
        service.service_description = request.form.get("service_description")
        service.price = request.form.get("price")
        db.session.commit()
        return redirect(url_for("services"))
    return render_template("edit_service.html", service=service)


@app.route("/delete_service/<int:service_id>")
def delete_service(service_id):
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    return redirect(url_for("services"))
