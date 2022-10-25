from flask import render_template
from app import app


@app.route("/")
def index():
    user_info = {
        'username' : 'Braxton',
        'email' : 'hiitsbraxton@gmail.com'
    }
    return render_template('index.html', user = user_info)



@app.route("/artists")
def get_artist():
    user_info = {
        'username' : 'Braxton',
        'email' : 'hiitsbraxton@gmail.com'
    }
    artists = ['j cole', 'the kid laroi', 'tupac', 'lil baby', 'drake']
    return render_template('artists.html', user = user_info, artists = artists)