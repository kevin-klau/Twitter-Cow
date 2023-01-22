from flask import Flask, render_template, request
app = Flask(__name__)

import os

@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/keke", methods=['GET','POST'])
def keke():
    if request.method == 'GET':
        os.system("python Scrape/keke.py")
        document_path = os.getcwd()+'/Scrape/ScrapedInfo.txt'
        document = open(document_path, 'r')
        with document as f:
            s = f.read()
            print(s)
        request.form = s

    return '<p>Bonjour</p>'
 
if __name__ == "__main__":
    app.run()