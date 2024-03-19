from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0',threaded = True)
