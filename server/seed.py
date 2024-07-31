from config import app, db
from models import Owner, Adoption_location, Dog

if __name__ == "__main__":

  with app.app_context():
    print("Starting Seeding")
    print('delete Owners...')
    Owner.query.delete()
    print('delete Adoption Locations...')
    Adoption_location.query.delete()
    print('delete Dogs...')
    Dog.query.delete()

    db.session.commit()

    print('creating owners...')
    owner_1 = Owner(name="Jason")
    owner_2 = Owner(name="Nate")
    owner_3 = Owner(name="Spencer")
    owner_4 = Owner(name="Dylan")
    owner_5 = Owner(name="None")

    owners = [owner_1, owner_2, owner_3, owner_4, owner_5 ]
    db.session.add_all(owners)
    db.session.commit()

    #Edit Below
    print('creating adoption locations...')
    adoption_location_1 = Adoption_location(name="NYC")
    adoption_location_2 = Adoption_location(name="Tennesse")
    adoption_location_3 = Adoption_location(name="Boston")
    adoption_location_4 = Adoption_location(name="Mexico")
    adoption_location_5 = Adoption_location(name="Unknown")

    adoption_locations = [adoption_location_1, adoption_location_2, adoption_location_3, adoption_location_4,adoption_location_5 ]

    db.session.add_all(adoption_locations)
    db.session.commit()

    print('creating dogs...')
    dog_1 = Dog(name="Loki", breed="Swiss Shepard", image= "https://mail.google.com/mail/u/0?ui=2&ik=928549f11f&attid=0.1&permmsgid=msg-a:r-5105516919894280834&th=18fbf8658d820f2e&view=fimg&fur=ip&sz=s0-l75-ft&attbid=ANGjdJ_zpP0rZugiFeIKmv7RjZgIryqOUd93HVHqs2uU0Ko91goriWVN55VWD2EAtEhCgnkeWYvJBawezst9q5a0p_AXz435T-13LFPR_bLi0c-9A1jYmBPNNY5CVC0&disp=emb&realattid=F00A2965-26E6-4667-A6E3-0A2398EFD208", owner_id =owner_1.id, adoption_location_id=adoption_location_1.id)
    dog_2 = Dog(name="Hans", breed="Bernese Mountain Dog",image= "https://mail.google.com/mail/u/0?ui=2&ik=928549f11f&attid=0.1&permmsgid=msg-a:r-3753084664028594781&th=18fc09d36b3e490d&view=fimg&fur=ip&sz=s0-l75-ft&attbid=ANGjdJ_z8pxM50sgp8Gon2yyehFcLKK52qe_-okxgEfZPRIF4fUn0oZrcP3JlHR_4hyMFVdqmd-4qhvKzo-nRg35e4k7b1AtVUStgVOuRhvhVR5fD8bV0i34Sgx0q4c&disp=emb&realattid=7AC242FF-3B2A-48C0-B4B9-E0A2CC383FC7", owner_id =owner_2.id, adoption_location_id=adoption_location_2.id)
    dog_3 = Dog(name="Sam", breed="Golden Retreiver", image= "https://www.vidavetcare.com/wp-content/uploads/sites/234/2022/04/golden-retriever-dog-breed-info.jpeg", owner_id =owner_3.id, adoption_location_id=adoption_location_3.id)
    dog_4 = Dog(name="Jofi", breed="King Charles Cavalier", image="https://www.hallettvet.com/sites/default/files/styles/large/public/cavalier-king-charles-spaniel-dog-breed-info.jpg?itok=djzA2ft0", owner_id =owner_4.id, adoption_location_id=adoption_location_4.id)
    dog_5 = Dog(name="George", breed="Black Labrador", image="https://cdn.britannica.com/82/232782-050-8062ACFA/Black-labrador-retriever-dog.jpg", owner_id =owner_3.id, adoption_location_id=adoption_location_3.id)

    dogs = [dog_1, dog_2, dog_3, dog_4, dog_5]

    db.session.add_all(dogs)
    db.session.commit()

    print('Finished Seeding')
