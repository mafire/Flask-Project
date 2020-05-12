# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: maf2299
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

#create links to different ruotes by making method after path
@app.route("/projects")
def proj():
    return render_template("projects.html")

@app.route("/experience")
def exp():
    return render_template("experience.html")
#start the server
if __name__ == "__main__":
    app.run()  