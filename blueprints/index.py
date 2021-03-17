import json
import requests
from flask import Flask, render_template,request
from flask import Blueprint

index = Blueprint('index', __name__)

@index.route('/')
@index.route('/index')
def indexfun():
    upcomingUrl = 'https://api.jikan.moe/v3/top/anime/1/upcoming'
    mostPopUrl = 'https://api.jikan.moe/v3/top/anime/1/bypopularity'
    upcoming = requests.get(upcomingUrl).json()['top']
    mostPop = requests.get(mostPopUrl).json()['top']
    return render_template('index.html', upcoming = upcoming, mostPop = mostPop, title = "Index")