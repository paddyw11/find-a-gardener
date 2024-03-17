from findagardener import db

class gardner_service_association(db.Model):
    #schema for the association model
    gardener_id = Column(Integer, ForeignKey('gardener.id'), primary_key=True)
    service_id = Column(Integer, ForeignKey('service.id'), primary_key=True)

class Service(db.Model):
    # schema for the Service model
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(25), unique=True, nullable=False)
    service_desciption = db.Column(db.text, nullable=False)
    price = db.Column(db.Integer)

    def __repr__(self):
        return self.service_name

class Gardener(db.Model):
    # schema for the Gardener model
    id = db.Column(db.Integer, primary_key=True)
    gardener_name = db.Column(db.String(50), unique=True, nullable=False)
    region_id = db.Column(db.ForeignKey("region.id", nullable=False))
    region =db.relationship("Region", backref=db.backref("gardeners", lazy=True))
    services_offered = db.Column(db.Integer, db.ForeignKey("service.id",), nullable=False)

class Region(db.Model):
    # schema for the region model
    id= db.Column(db.Integer, primary_key=True)
    region_name = db.Column(db.String(50), unique=True, nullable=False)