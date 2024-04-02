from findagardener import db

class GardenerServiceAssociation(db.Model):
    # schema for the association model
    gardener_id = db.Column(db.Integer, db.ForeignKey('gardener.id'), primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), primary_key=True)

class Service(db.Model):
    # schema for the Service model
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(25), unique=True, nullable=False)
    service_description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer)

    def __repr__(self):
        return self.service_name

class Gardener(db.Model):
    # schema for the Gardener model
    id = db.Column(db.Integer, primary_key=True)
    gardener_name = db.Column(db.String(50), unique=True, nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey("region.id"), nullable=False)
    region = db.relationship("Region", backref=db.backref("gardener", lazy=True))
    services_offered = db.relationship("Service", secondary='gardener_service_association')

    def __repr__(self):
        return "#{0} - Gardener: {1} | Region: {2}".format(
            self.id, self.gardener_name, self.region.region_name
        )

class Region(db.Model):
    # schema for the region model
    id = db.Column(db.Integer, primary_key=True)
    region_name = db.Column(db.String(50), unique=True, nullable=False)

    def region_id(self):
        return self.id

    def __repr__(self):
        return self.region_name