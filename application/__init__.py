from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import pymysql

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personaltrainer-db.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todoapp-db.db'
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DB_URI")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SECRET_KEY'] = 'qaqaqaqa'

db = SQLAlchemy(app)

import application.routes