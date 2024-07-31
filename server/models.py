from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from config import db

class Owner(db.Model, SerializerMixin):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    dogs = db.relationship('Dog', back_populates='owner', cascade='all, delete-orphan')
    adoption_location = association_proxy('dogs', 'adoption_location', creator= lambda adoption_location_obj: Dog(adoption_location=adoption_location_obj))

    serialize_rules=('-dogs.owner',)

    def __repr__(self):
        return f"<Owner {self.name}>"

class Adoption_location(db.Model, SerializerMixin):
    __tablename__ = "adoption_locations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    dogs = db.relationship('Dog', back_populates='adoption_location', cascade='all, delete-orphan')
    owner = association_proxy('dogs', 'owner', creator= lambda owner_obj: Dog(owner=owner_obj))

    serialize_rules=('-dogs.adoption_location',)

    def __repr__(self):
        return f"<Adoption_location {self.name}>"
    
class Dog(db.Model, SerializerMixin):
    __tablename__ = "dogs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    breed = db.Column(db.String)
    image = db.Column(db.String)

    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id')) 
    adoption_location_id = db.Column(db.Integer, db.ForeignKey('adoption_locations.id'))

    owner = db.relationship('Owner', back_populates= 'dogs')
    adoption_location = db.relationship('Adoption_location', back_populates= 'dogs')

    serialize_rules=('-owner.dogs','-adoption_location.dogs')
    
    def __repr__(self):
        return f"<Dog {self.name}, {self.breed}, {self.image} >"