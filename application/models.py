from application import db



class Trainer(db.Model):
    trainer_id = db.Column(db.Integer, primary_key = True)
    forename = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    skill = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    assigned_to = db.relationship('Workout', backref='trainer')
    def __str__(self):
        return f"{self.forename} {self.surname}: {self.skill.upper()}. £{self.price}0ph"

class Client(db.Model):
    client_id = db.Column(db.Integer, primary_key = True)
    forename = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    fitness_level = db.Column(db.Integer, nullable=False)
    assigned_to = db.relationship('Workout', backref='client')
    def __str__(self):
         return f"{self.forename}, {self.surname}, {self.age}, {self.address}, {self.email}: Fitness level: ({self.fitness_level} out of 10)"

class Workout(db.Model):
    workout_id = db.Column(db.Integer, primary_key = True)
    workout_date = db.Column(db.Date, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.client_id'))
    assigned_to = db.Column(db.Integer, db.ForeignKey('trainer.trainer_id'))
    
    def __str__(self):
        return f"Session booked for: {self.client.forename + ' ' + self.client.surname} on {self.workout_date} with the trainer {self.trainer.forename + ' ' + self.trainer.surname} costing £{self.trainer.price}0"

        # ----------------------- 