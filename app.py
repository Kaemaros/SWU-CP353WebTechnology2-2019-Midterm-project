import json
import requests
from flask import Flask, render_template,request,Blueprint
from database import db, students

from blueprints.aboutus import aboutus
from blueprints.genre import genre 
from blueprints.index import index
from blueprints.info import info
from blueprints.mostPopular import mostPopular
from blueprints.search import search
from blueprints.upComing import upComing

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app) 

@app.before_first_request
def create_table():
    db.create_all()
 
app.register_blueprint(aboutus)
app.register_blueprint(genre)
app.register_blueprint(index)
app.register_blueprint(info)
app.register_blueprint(mostPopular)
app.register_blueprint(search)
app.register_blueprint(upComing)

