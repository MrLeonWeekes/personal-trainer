from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from datetime import date

class checkDateInFuture():
    def __init__(self, message):
        self.message = message
    
    def __call__(self, form, field):
        if field.data < date.today():
            raise ValidationError(self.message)

        # ----------------------- 

class ClientForm(FlaskForm):
    forename = StringField('Forename', validators=[DataRequired(), Length(min=1, max=30)])
    surname = StringField('Surname', validators=[DataRequired(), Length(min=1, max=30)])
    dob = DateField('Date Of Birth', validators=[DataRequired(), checkDateInFuture("Please choose a date in the future")])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Email', validators=[DataRequired(), Length(min=1, max=50)])
    fitness_level = StringField('Fitness Level (1 to 10)', validators=[DataRequired(), Length(min=1, max=2)])
    submit = SubmitField('Enter')

class TrainerForm(FlaskForm):
    forename = StringField('Forename', validators=[DataRequired(), Length(min=1, max=30)])
    surname = StringField('Surname', validators=[DataRequired(), Length(min=1, max=30)])
    skill = StringField('Skill', validators=[DataRequired(), Length(min=1, max=50)])
    price = StringField('Price', validators=[DataRequired(), Length(min=1, max=10)])
    submit = SubmitField('Enter')

class WorkoutForm(FlaskForm):
    workout_date = DateField('Select a date to workout', validators=[DataRequired(), checkDateInFuture("Please choose a date in the future")])

        # ----------------------- 