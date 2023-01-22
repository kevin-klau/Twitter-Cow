from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)

import os

@app.route("/receiver",methods=["POST"])
def post():
    data = request.get_json()
    data = jsonify(data)
    return data

@app.route("/", methods=['GET','POST'])
def index():
    return render_template("testhtml.html")

@app.route("/keke", methods=['GET','POST'])
def keke():
    # os.system("python Scrape/keke.py")
    # os.system("python3 Scrape/keke.py")
    scrape()
    document_path = os.getcwd()+'/Scrape/ScrapedInfo.txt'
    document = open(document_path, 'r')
    with document as f:
        s = f.read()
    #keke.scrape()
    return '<p>Bonjour</p>'
 
if __name__ == "__main__":
    app.run(debug=True)

import os
import snscrape
import pandas as pd
import snscrape.modules.twitter as sntwitter
import csv
import numpy as np

def scrape() -> None:
    tweets_list1 = set()

    # Using TwitterSearchScraper to scrape data and append tweets to list
    hashtag : str

    with open('ScrapedInfo.txt', 'w', encoding='utf-8') as f:

        for i,tweet in enumerate(sntwitter.TwitterSearchScraper('hashtag').get_items()):
            if i>500:
                break
            info = tweet.content + 'とチ.く$' + str(tweet.replyCount) + 'とチ.く$' + str(tweet.likeCount) + 'とチ.く$' + str(tweet.retweetCount) + 'とチ.く$' + str(tweet.quoteCount) + 'とチ.く$' + str(tweet.viewCount) + 'ン'
            for i in info : 
                if ord(i) == 32 or ord(i) == 35:
                    continue
                elif ord(i) == 12531:
                    break
                else:
                    f.write(i)