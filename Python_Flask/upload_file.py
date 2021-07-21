from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from pandas.errors import ParserError
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
        file = request.form
        print(type(file))
        data = []
        # with open(f) as file:
        # csvfile = csv.reader(file)
        try:
            csvfile = pd.read_csv(file)
        except ParserError as err:
            msg = "File type is Incorrect as appropriate type should be '.csv' or file is corrupted"
            return render_template('file_upload.html')   #,msg=msg)
        except ValueError as err:
            return render_template('file_upload.html')
        else:
            for line in csvfile:
                data.append(line)
            return {'data':data}
        # return render_template('data.html',data=data)
        # print(type({'data':data})) # TypeError
        # return render_template('data.html', data=json.dumps(data, indent=2))

# @app.route('/upload', methods=['POST','GET'])
# def upload():
#     # if request.method == 'POST':
#     return "<h1>File Uploaded Successfull !!!</h1>"
## Here i am facing problem with post method as post doesnot returns string as above

if __name__ == '__main__':
    app.run(debug=True)
