import json
import requests
from flask import Flask, render_template,request
from flask import Blueprint

aboutus = Blueprint('aboutus', __name__)

@aboutus.route('/aboutus')
def aboutusfun():
    return render_template('aboutus.html',title = "aboutus")