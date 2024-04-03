from flask import render_template, request, redirect, url_for, flash
from findagardener import app, db
from findagardener.models import GardenerServiceAssociation, Service, Gardener, Region

from werkzeug.security import generate_password_hash, check_password_hash

#db.drop_all()
db.create_all()

#from findagardener.models import Category, Task

@app.route("/")
def home():
    return render_template("gardeners.html")

#register 

@app.route("/register", methods=["GET", "POST"])
def register():
#    if request.method == "POST":
#        #check if username already exists in db
 #   existing_user =
    return render_template("register.html")

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

@app.route("/gardeners")
def gardeners():
    gardeners = list(Gardener.query.order_by(Gardener.gardener_name).all())
    return render_template("gardeners.html", gardeners=gardeners)


@app.route("/add_gardener", methods=["GET", "POST"])
def add_gardener():

    services = Service.query.order_by(Service.service_name).all()
    regions = Region.query.order_by(Region.region_name).all()
    
    if request.method == "POST":
        # Extract form data
        gardener_name = request.form.get("gardener_name")
        region_id = int(request.form.get("region_id"))
        services_offered = [int(service_id) for service_id in request.form.getlist("services_offered")]

         # Check if gardener with the same name already exists
        existing_gardener = Gardener.query.filter_by(gardener_name=gardener_name).first()
        if existing_gardener:
            flash('A gardener with this name already exists!')
            return redirect(url_for("add_gardener"))

        # Get the region object based on the region ID from the form
        region = Region.query.get(region_id)

        # Get the service objects based on the service IDs from the form
        services = Service.query.filter(Service.id.in_(services_offered)).all()
              
         # Create a new gardener object
        gardener = Gardener(
            gardener_name=gardener_name,
            region=region,
            services_offered=services
        )

        db.session.add(gardener)
        db.session.commit()

        flash("Gardener added successfully")
        print("Gardener added successfully") 
        return redirect(url_for("gardeners"))

    # For GET request, render the add_gardener template
    services = Service.query.order_by(Service.service_name).all()
    regions = Region.query.order_by(Region.region_name).all()
    return render_template("add_gardener.html", services=services, regions=regions)
    

@app.route("/edit_gardener/<int:gardener_id>", methods=["GET", "POST"])
def edit_gardener(gardener_id):
    gardener = Gardener.query.get_or_404(gardener_id)
    regions = Region.query.order_by(Region.region_name).all()
    services = Service.query.order_by(Service.service_name).all()
    if request.method == "POST":
        gardener_name = request.form.get("gardener_name")
        region_id = int(request.form.get("region_id"))
        services_offered = [int(service_id) for service_id in request.form.getlist("services_offered")]
        
        db.session.commit()
        return redirect(url_for("gardeners"))
        
    return render_template("edit_gardener.html", services=services, regions=regions, gardener=gardener)

@app.route("/delete_gardener/<int:gardener_id>")
def delete_gardener(gardener_id):
    gardener = Gardener.query.get_or_404(gardener_id)
    db.session.delete(gardener)
    db.session.commit()
    return redirect(url_for("gardeners"))

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
        db.session.commit()
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