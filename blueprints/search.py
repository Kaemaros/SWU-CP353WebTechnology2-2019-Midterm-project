import json
import requests
from flask import Flask, render_template,request
from flask import Blueprint

search = Blueprint('search', __name__)

@search.route('/search/')
def searchfunfun():
    keyword = request.args.get('keyword', default = '')
    url = 'https://api.jikan.moe/v3/search/anime?q=' + keyword
    try:
        search = requests.get(url).json()['results']
        if search:
            return render_template('search.html', search = search, title = "Search : " + keyword)            
        else:
            raise Exception()
    except:
        return render_template('NoResult.html',title ='No Result')