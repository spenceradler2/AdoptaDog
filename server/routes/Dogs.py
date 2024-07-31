from flask import request
from config import db, api 
# from config import app

from flask_restful import Resource
from models import Dog, Owner, Adoption_location
from sqlalchemy.exc import IntegrityError

class DogsResource(Resource):
    def get(self):
        dogs = [dog.to_dict() for dog in Dog.query.all()]
        return dogs, 200
    
    def post(self):
      data = request.get_json()
      name = data.get("name")
      breed = data.get("breed")
      image = data.get("image")
      owner_name = data.get("owner_name")
      adoption_location_name = data.get("adoption_location_name")
       
      if Owner.query.filter_by(name=owner_name).first():
        owner = Owner.query.filter_by(name=owner_name).first()
        owner_id = owner.id
      else:
        owner = Owner(name=owner_name)
        db.session.add(owner)
        db.session.commit()
        owner_id = owner.id

      if Adoption_location.query.filter_by(name=adoption_location_name).first():
        adoption_location = Adoption_location.query.filter_by(name=adoption_location_name).first()
        adoption_location_id = adoption_location.id
      else:
        adoption_location = Adoption_location(name=adoption_location_name)
        db.session.add(adoption_location)
        db.session.commit()
        adoption_location_id = adoption_location.id

      dog = Dog(name=name, breed=breed, image=image, owner_id=owner_id,adoption_location_id=adoption_location_id )
      db.session.add(dog)
      db.session.commit() 
             
      return dog.to_dict(), owner.to_dict(), adoption_location.to_dict(), 201
      #Review to add validations
        
api.add_resource(DogsResource, "/dogs", endpoint="dogs")

class DogResource(Resource):
  def get(self, id):
    dog = Dog.query.get(id)
    return dog.to_dict(), 200
  
  def patch(self, id):
    data = request.get_json()
    try:
      for key, value in data.items():
        dog = Dog.query.get(id)
        if hasattr(dog, key):
          setattr(dog, key, value)
        else:
          return {"message": f"{key} is not an attribute of Dog"}, 422
      db.session.add(dog)
      db.session.commit()
      return dog.to_dict(), 200
    # Review
    except IntegrityError as e:
      return {"error": e.orig.args[0]}, 422
    except ValueError as e:
      return {"error": str(e)}, 422
  
  def delete(self, id):
    dog = Dog.query.get(id)
    db.session.delete(dog)
    db.session.commit()
    return {}, 204


api.add_resource(DogResource, "/dogs/<int:id>", endpoint="dog")