from flask import render_template, request, redirect, url_for, flash, session
from findagardener import app, db
from findagardener.models import GardenerServiceAssociation, Service, \
    Gardener, Region, Users

from werkzeug.security import generate_password_hash, check_password_hash

db.create_all()


@app.route("/")
def home():
    return render_template("home.html")

# register


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = Users.query.filter(
            Users.username == request.form.get("username").lower()).all()

        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register"))

        user = Users(
            username=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
            )
        db.session.add(user)
        db.session.commit()

        # puts the new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("You have successfully registered!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = Users.query.filter(Users.username == request.form.get(
            "username").lower()).all()

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user[0].password, request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    A function that displays the user's gardener profile
    they have created
    """
    if "user" in session:
        """
        Checks if the user is logged in, retrieves their username
        and displays their profile
        """
        gardeners = list(Gardener.query.order_by(Gardener.gardener_name).all())
        return render_template(
            "profile.html", username=session["user"], gardeners=gardeners)

    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Function that clears the session data to log the user out
    and redirect to the log in page
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/full_profile/<gardener_name>")
def full_profile(gardener_name):
    """
    A function to dipslay the full prfile of the the gardener.
    """
    gardener = Gardener.query.filter_by(gardener_name=gardener_name).first()
    return render_template("full_profile.html", gardener=gardener)


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

# gardener


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
        services_offered = [
            int(service_id) for service_id in
            request.form.getlist("services_offered")]
        created_by = session.get("user")

        # Check if gardener with the same name already exists
        existing_gardener = Gardener.query.filter_by(
            gardener_name=gardener_name).first()
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
            services_offered=services,
            created_by=created_by
        )

        db.session.add(gardener)
        db.session.commit()

        flash("Gardener added successfully")
        print("Gardener added successfully")
        return redirect(url_for("gardeners"))

    # For GET request, render the add_gardener template
    services = Service.query.order_by(Service.service_name).all()
    regions = Region.query.order_by(Region.region_name).all()
    return render_template("add_gardener.html", services=services,
                           regions=regions)


@app.route("/edit_gardener/<int:gardener_id>", methods=["GET", "POST"])
def edit_gardener(gardener_id):
    gardener = Gardener.query.get_or_404(gardener_id)
    regions = Region.query.order_by(Region.region_name).all()
    services = Service.query.order_by(Service.service_name).all()
    if request.method == "POST":
        gardener_name = request.form.get("gardener_name")
        region_id = int(request.form.get("region_id"))
        services_offered = [int(service_id) for service_id
                            in request.form.getlist("services_offered")]

        gardener.gardener_name = gardener_name
        gardener.region_id = region_id
        gardener.services_offered = Service.query.filter(Service.id.in_(
            services_offered)).all()
        db.session.commit()
        return redirect(url_for("gardeners"))

    return render_template("edit_gardener.html", services=services,
                           regions=regions, gardener=gardener)


@app.route("/delete_gardener/<int:gardener_id>")
def delete_gardener(gardener_id):
    gardener = Gardener.query.get_or_404(gardener_id)
    db.session.delete(gardener)
    db.session.commit()
    return redirect(url_for("gardeners"))

# region code


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


@app.route("/gardeners_by_region/<int:region_id>")
def gardeners_by_region(region_id):
    # Displays the gardeners for the selected region
    gardeners = list(Gardener.query.order_by(Gardener.gardener_name).all())
    region = Region.query.get_or_404(region_id)
    return render_template("gardeners_by_region.html",
                           region=region, gardeners=gardeners,
                           regions=regions)


@app.route("/gardeners_by_service/<int:service_id>")
def gardeners_by_service(service_id):
    # Displays the gardeners for the selected service
    gardeners = Gardener.query.filter(Gardener.services_offered.any(
        id=service_id)).all()
    service = Service.query.get_or_404(service_id)
    return render_template("gardeners_by_service.html",
                           service=service, gardeners=gardeners,
                           services_offered=services)
