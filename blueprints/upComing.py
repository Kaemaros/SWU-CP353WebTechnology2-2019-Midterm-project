import json
import requests
from flask import Flask, render_template,request
from flask import Blueprint

upComing = Blueprint('upComing', __name__)

@upComing.route('/Upcoming/<page>')
def upComingfun(page):
    page = int(page)
    try:
        upcoming = requests.get('https://api.jikan.moe/v3/top/anime/{}/upcoming'.format(page)).json()['top']
        if upcoming:
            return render_template('upcoming.html', data = upcoming,nextPage = page+1, title = "Upcoming")        
        else:
            raise Exception()
    except:
        return render_template('NoResult.html',title ='No Result')