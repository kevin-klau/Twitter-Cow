from flask import Flask, render_template, request, jsonify
#from flask_cors import CORS
app = Flask(__name__)
#cors = CORS(app)

import os
import snscrape
import pandas as pd
import snscrape.modules.twitter as sntwitter
import csv
import numpy as np
import math
import json
import random

@app.route("/receiver",methods=["POST"])
def post():
    data = request.get_json()
    data = jsonify(data)
    return data

@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/keke/<string:searchQuery>", methods=['GET','POST'])
def keke(searchQuery):
    searchQuery=json.loads(searchQuery)
    data=searchQuery
    scrape(data)
    document_path = os.getcwd()+'/Scrape/ScrapedInfo.txt'
    document = open(document_path, 'r')
    with document as f:
        s = f.read()
    c = algorithm(s)
    

    return '<p>Bonjour</p>'
 
if __name__ == "__main__":
    app.run(debug=True)

def algorithm (text : str) -> int:
    posts = text.split('ンチミマチ')
    
    with open("data.csv",'r') as f :
        data_list = list(csv.reader(f, delimiter=","))

    theSet = {}
    for j in posts:
        i = 0
        if j == "" : continue
        while i < len(data_list):
            if data_list[i][0] in j :
                information = j.split('とチ.く$')
                #adder = math.log(6 * float(information[1]) + 1,5) + math.log(6 * float(information[2]) + 1,5) + math.log(10 * float(information[3]) + 1,5) + math.log(10 * float(information[4]) + 1,5)
                adder = random.randint(0, 30)
                print(information[1])
                if data_list[i][0] in theSet:
                    theSet[data_list[i][0]] += adder
                else :
                    theSet[data_list[i][0]] = adder
                    print(theSet[data_list[i][0]])
            i += 1

    theSet = sorted(theSet.items())
    theSet.sort(key=lambda y: y[1], reverse=True)
    dictionary = {}
    for k in range(1,6):
        print(k)
        print(theSet)
        dictionary[theSet[k][0]] = theSet[k][1]
        
    with open("sample.json", "w") as outfile:
        json.dump(dictionary, outfile)


def scrape(vart:str) -> None:
    tweets_list1 = set()

    # Using TwitterSearchScraper to scrape data and append tweets to list
    hashtag : str

    with open('ScrapedInfo.txt', 'w', encoding='utf-8') as f:

        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(vart + ' min_faves:50 ').get_items()):
            if i>500:
                break
            f.write(tweet.content + 'とチ.く$' + str(tweet.replyCount) + 'とチ.く$' + str(tweet.likeCount) + 'とチ.く$' + str(tweet.retweetCount) + 'とチ.く$' + str(tweet.quoteCount) + 'とチ.く$' + str(tweet.viewCount) + 'ンチミマチ')
