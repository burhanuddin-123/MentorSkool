from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    # return "<h1>Hello, Burhanuddin !!!!</h1>"

@app.route('/welcome')
#http://localhost:5000/welcome
def welcome():
    # return render_template('index.html')
    return "<h1>Hello, Burhanuddin !!!!</h1>"

@app.route('/register')
def registration():
    return render_template('Registration.html')

@app.route('/register_success',methods=['POST','GET'])
def register_success():
    if request.method == 'POST':
        result = request.form
        return render_template('register_data.html', result=result)

# if __name__ == "__main__":
#     app.run(debug=True)
