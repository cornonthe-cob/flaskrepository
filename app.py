from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index(name):
	return '<h1>Hello!</h1>'