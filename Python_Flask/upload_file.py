from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from pandas.errors import ParserError
import csv
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('file_upload.html')

@app.route('/upload', methods=['GET','POST'])
def data():
    if request.method == 'POST':
        file = request.files['csv']
        name = file.filename
        if name.endswith('.csv'):
            if not os.path.isdir('static'):
                os.mkdir('static')
            filepath = os.path.join('static', file.filename)
            file.save(filepath)
            data = []
            with open(f"static/{name}") as file:
                csvfile = csv.reader(file)
                for line in csvfile:
                    data.append(line)
            return {'data':data}
        else:
            return render_template('file_upload.html', msg="Not a csv file")  ## mistake as we have to redirect url to home

if __name__ == '__main__':
    app.run(debug=True)
