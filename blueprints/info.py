import json
import requests
from flask import Flask, render_template,request
from flask import Blueprint

info = Blueprint('info', __name__)

@info.route('/info/<id>')
def infofun(id):
    data = requests.get('https://api.jikan.moe/v3/anime/' + id).json()
    return render_template('info.html',data = data,title = data['title'])
        
    