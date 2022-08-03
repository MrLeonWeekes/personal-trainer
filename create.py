from application import db
from application.models import Client, Trainer, Workout
from datetime import date

# db.drop_all()
db.create_all()

client1 = Client(forename="Tim", surname="Mole", age=45, address="12 Lindsey St", email="tm@email.com", fitness_level=9)
trainer1 = Trainer(forename="Mark", surname="Ramsey", skill="fitness", price=120)
workout1 = Workout(client_id=1, trainer_id=1, workout_date=date(2022, 8, 6)) 
client2 = Client(forename="Keith", surname="Gill", age=49, address="212 Friday St", email="kg@email.com", fitness_level=3)

db.session.add(client1)
db.session.add(trainer1)
db.session.add(workout1)
db.session.add(client2)
db.session.commit()

print(client1)
print(trainer1)
print(workout1)
print(workout1.client)
print(client2)