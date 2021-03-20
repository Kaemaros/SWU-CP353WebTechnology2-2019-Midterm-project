import json
import requests
from flask import Flask, render_template,request
from flask import Blueprint

genre = Blueprint('genre', __name__)

genreId = {
        'Action': 1,
        'Adventure': 2,
        'Cars': 3,
        'Comedy': 4,
        'Dementia': 5,
        'Demons': 6,
        'Mystery': 7,
        'Drama': 8,
        'Ecchi': 9,
        'Fantasy': 10,
        'Game': 11,
        'Hentai': 12,
        'Historical': 13,
        'Horror': 14,
        'Kids': 15,
        'Magic': 16,
        'Martial Arts': 17,
        'Mecha': 18,
        'Music': 19,
        'Parody': 20,
        'Samurai': 21,
        'Romance': 22,
        'School': 23,
        'Sci Fi': 24,
        'Shoujo': 25,
        'Shoujo Ai': 26, 
        'Shounen': 27,
        'Shounen Ai': 28, 
        'Space': 29,
        'Sports': 30, 
        'Super Power': 31,
        'Vampire': 32,
        'Yaoi': 33,
        'Yuri': 34,
        'Harem': 35,
        'Slice Of Life': 36,
        'Supernatural': 37,
        'Military': 38,
        'Police': 39,
        'Psychological': 40,
        'Thriller': 41,
        'Seinen': 42,
        'Josei': 43
    }

@genre.route('/genre/')
def genre_select():
    return render_template('genre.html', title = 'Genre')
@genre.route('/genre/<genre>/<page>')
def genre_pages(genre,page):
    page = int(page)
    try:
        data = requests.get('https://api.jikan.moe/v3/genre/anime/' + str(genreId[genre]) + '/' + str(page)).json()['anime']
        if data:
            return render_template('genre_selected.html',data = data, nextPage = page + 1,title = genre)            
        else:
            raise Exception()
    except:
        return render_template('NoResult.html',title ='No Result')