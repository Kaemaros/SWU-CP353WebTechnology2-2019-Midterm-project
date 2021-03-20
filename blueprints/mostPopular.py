import json
import requests
from flask import Flask, render_template,request
from flask import Blueprint

mostPopular = Blueprint('mostPopular', __name__)

@mostPopular.route('/MostPopular/<page>')
def mostPopularfun(page):
    page = int(page)
    try:
        mostPop = requests.get('https://api.jikan.moe/v3/top/anime/{}/bypopularity'.format(page)).json()['top']
        if mostPop:
            return render_template('mostPop.html', data = mostPop, nextPage = page+1, title = "MostPopular")      
        else:
            raise Exception()
    except:
        return render_template('NoResult.html',title ='No Result')