from application import db



class Trainer(db.Model):
    trainer_id = db.Column(db.Integer, primary_key = True)
    forename = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    skill = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    wk1 = db.relationship('Workout', backref='trainer')
    def __str__(self):
        return f"{self.forename} {self.surname}: {self.skill.upper()}. £{self.price}0ph"

class Client(db.Model):
    client_id = db.Column(db.Integer, primary_key = True)
    forename = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    fitness_level = db.Column(db.Integer, nullable=False)
    wk2 = db.relationship('Workout', backref='client')
    def __str__(self):
         return f"{self.forename}, {self.surname}, {self.dob}, {self.address}, {self.email}: Fitness level: ({self.fitness_level} out of 10)"

class Workout(db.Model):
    workout_id = db.Column(db.Integer, primary_key = True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.client_id'))
    # client_forename = db.Column(db.String(50), db.ForeignKey('client.forename'))
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.trainer_id'))
    workout_date = db.Column(db.Date, nullable=False)
    def __str__(self):
        return f"Session booked for: {self.client.forename + ' ' + self.client.surname} on {self.workout_date} with the trainer {self.trainer.forename + ' ' + self.trainer.surname} costing £{self.trainer.price}0"

        # ----------------------- 