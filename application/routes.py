from application import app, db
from application.models import *
from datetime import date, timedelta
from flask import request, redirect, url_for, render_template
from application.forms import *

@app.route('/')
def index():
    return render_template('layout.html')



@app.route('/delete-client/<int:id>')
def delete_client(id):
    client_to_delete = Client.query.get(id)
    db.session.delete(client_to_delete)
    db.session.commit()
    return redirect(url_for('view_all_clients'))



@app.route('/add-client', methods=['GET', 'POST'])
def add_client():
    form = ClientForm()
    if form.validate_on_submit():
        forename = form.forename.data
        surname = form.surname.data
        age = form.age.data
        address = form.address.data
        email = form.email.data
        fitness_level = form.fitness_level.data
        new_client = Client(forename=forename, surname=surname, age=age, address=address, email=email, fitness_level=fitness_level)
        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for('view_all_clients'))
    return render_template('client_form.html', form=form)

@app.route('/view-clients')
def view_all_clients():
    clients = Client.query.all()
    return render_template('view_all_clients.html', entity='Client', tasks=clients)

@app.route('/update-client/<int:id>', methods=['GET', 'POST'])
def update_client(id):
    client_to_update = Client.query.get(id)
    form = ClientForm()
    # users = Client.query.all()
    # form.assigned_to.choices = [(user.client_id, f"{user.forename} {user.surname}") for user in users]
    if form.validate_on_submit():
        client_to_update.forename = form.forename.data
        client_to_update.surname = form.surname.data
        client_to_update.age = form.age.data
        client_to_update.address = form.address.data
        client_to_update.email = form.email.data
        client_to_update.fitness_level = form.fitness_level.data
        db.session.commit()
        return redirect(url_for('view_all_clients'))
    form.forename.data = client_to_update.forename
    form.surname.data = client_to_update.surname
    form.age.data = client_to_update.age
    form.address.data = client_to_update.address
    form.email.data = client_to_update.email
    form.fitness_level.data = client_to_update.fitness_level
    return render_template('client_form.html', form=form)

@app.route('/add-trainer', methods=['GET', 'POST'])
def add_trainer():
    form = TrainerForm()
    if form.validate_on_submit():
        forename = form.forename.data
        surname = form.surname.data
        skill = form.skill.data
        price = form.price.data
        new_trainer = Trainer(forename=forename, surname=surname, skill=skill, price=price)
        db.session.add(new_trainer)
        db.session.commit()
        return redirect(url_for('view_all_trainers'))
    return render_template('trainer_form.html', form=form)

@app.route('/view-trainers')
def view_all_trainers():
    trainers = Trainer.query.all()
    return render_template('view_all_trainers.html', entity='Trainer', tasks=trainers)

# @app.route('/workout', methods=['GET', 'POST'])
# def book_workout():
#     form = WorkoutForm()
#     if form.validate_on_submit():
