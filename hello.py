from flask import Flask, render_template
 
app = Flask(__name__)

import os

@app.route("/")
def index():
    document_path = os.getcwd()+'/Scrape/ScrapedInfo.txt'
    document = open(document_path, 'r')
    with document as f:
        s = f.read()
    print(s)
    return render_template("index.html")
 
if __name__ == "__main__":
    app.run()