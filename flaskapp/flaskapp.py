from flask import Flask, render_template, url_for
import pandas as pd
import os

app = Flask(__name__)

@app.route("/styles.css")
def styles():
    return url_for('static', filename='styles.css')

@app.route('/')
def home():
    file=url_for('static', filename='about9.jpg')
    return render_template('flaskapp.html', file=file)

if __name__ == "__main__":
    app.run()