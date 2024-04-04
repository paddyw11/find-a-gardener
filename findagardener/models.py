from findagardener import db


class Users(db.Model):
    #schema for the users model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(500), unique=True, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - username: {1} | password: {2}".format(
            self.username, self.password)

# schema for the association model
GardenerServiceAssociation = db.Table('gardener_service_association',
                                            db.Column('gardener_id', db.Integer, db.ForeignKey('gardener.id', ondelete="CASCADE"), primary_key=True),
                                            db.Column('service_id', db.Integer, db.ForeignKey('service.id', ondelete="CASCADE"), primary_key=True)
                                            )

class Service(db.Model):
    # schema for the Service model
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(50), unique=True, nullable=False)
    service_description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer)

    def __repr__(self):
        return self.service_name

class Gardener(db.Model):
    # schema for the Gardener model
    id = db.Column(db.Integer, primary_key=True)
    gardener_name = db.Column(db.String(50), unique=True, nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey("region.id", ondelete="CASCADE"), nullable=False)
    region = db.relationship("Region", backref=db.backref("gardener"), lazy=True)
    services_offered = db.relationship("Service", secondary='gardener_service_association', backref='gardeners')

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