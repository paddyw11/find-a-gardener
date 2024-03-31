from flask import render_template, request, redirect, url_for
from findagardener import app, db
from findagardener.models import GardenerServiceAssociation, Service, Gardener, Region
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

#gardener
@app.route("/add_gardener", methods=["GET", "POST"])
def add_gardener():
    services = list(Service.query.order_by(Service.service_name).all())
    regions = Region.query.all()
    if request.method == "POST":
        gardener = Gardener(
            gardener_name=request.form.get("gardener_name"),
            region=request.form.get("region.region_name",),
            services_offered=request.form.getlist("services_offered")
        )
        db.session.add(gardener)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_gardener.html", services=services, regions=regions)


#region code
@app.route("/region")
def regions():
    regions = Region.query.order_by(Region.region_name).all()
    return render_template("regions.html", regions=regions)


@app.route("/add_region", methods=["GET", "POST"])
def add_region():
    if request.method == "POST":
        region = Region(
            region_name=request.form.get("region_name")
        )
        db.session.add(region)
        return redirect(url_for("regions"))
    return render_template("add_region.html")


@app.route("/edit_region/<int:region_id>", methods=["GET", "POST"])
def edit_region(region_id):
    region = Region.query.get_or_404(region_id)
    if request.method == "POST":
        region.region_name = request.form.get("region_name")
        db.session.commit()
        return redirect(url_for("regions"))
    return render_template("edit_region.html", region=region)


@app.route("/delete_region/<int:region_id>")
def delete_region(region_id):
    region = Region.query.get_or_404(region_id)
    db.session.delete(region)
    db.session.commit()
    return redirect(url_for("regions"))