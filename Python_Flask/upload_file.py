from flask import Flask, render_template, request
import pandas as pd
import csv
from werkzeug.utils import secure_filename
import json

# from werkzeug import secure_filename # not available
# from werkzeug.datastructures import  FileStorage # Explore more about this

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('file_upload.html')

@app.route('/upload', methods=['GET','POST'])
def data():
    if request.method == 'POST':
        f = request.form['csv']
        data = []
        with open(f) as file:
            csvfile = csv.reader(file)
            for line in csvfile:
                data.append(line)
        print(data)
        return {'data':data}
        # return render_template('data.html', data=json.dumps(data, indent=2))

# @app.route('/upload', methods=['POST','GET'])
# def upload():
#     # if request.method == 'POST':
#     return "<h1>File Uploaded Successfull !!!</h1>"
## Here i am facing problem with post method as post doesnot returns string as above

if __name__ == '__main__':
    app.run(debug=True)