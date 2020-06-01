# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 17:12:58 2020

@author: giovanni
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")


app.run()