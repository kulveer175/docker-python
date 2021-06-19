from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'CST Docker Mid Term Exam'

@app.route('/about')
def about():
    return 'This is Kulveer'

@app.route('/contact')
def contact():
    return 'My Id is: 201909145'