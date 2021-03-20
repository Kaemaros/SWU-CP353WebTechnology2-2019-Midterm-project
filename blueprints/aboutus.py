import json
import requests
from flask import Flask, render_template,request
from flask import Blueprint
from database import students

aboutus = Blueprint('aboutus', __name__)

@aboutus.route('/aboutus')
def aboutusfun():
    return render_template('aboutus.html',title = "aboutus", students=students.query.all())