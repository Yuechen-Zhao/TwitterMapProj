"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, jsonify
from TwitterMapProj import app
#from elasticsearch import ElasticSearch
from pyes import *
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

conn = ES()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""

    return render_template(
        'mainTwitterMap.html',
        title='Main Twitter Map Page',
        year=datetime.now().year,
    )

@app.route('/getTwits/<keyword>')
def get_tweets(keyword):
    keyword = keyword.encode('utf-8')
    data = []
    # SHOULD HERE BE A TIME LIMIT????????
    q = TermQuery('key', keyword)
    results = conn.search(query = q)

    for line in results:
        data.append(line)
    return jsonify({'data':data})