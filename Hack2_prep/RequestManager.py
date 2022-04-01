from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from markupsafe import re
import Authenticate
import os
app = Flask(__name__)
# AUTHENTICATOR_IP= os.getenv("AUTHENTICATOR_IP")
# AUTHENTICATOR_PORT= os.getenv("AUTHENTICATOR_PORT")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Actor.db'
db = SQLAlchemy(app)

class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(60), nullable=False)



@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/signup/<role>',methods=["POST"])
def signup(role):
    return jsonify(Authenticate.signup(role,request,db,Actor))

@app.route('/login/<role>',methods=["POST"])
def login(role):
    return jsonify(Authenticate.login(role,request,Actor))

if __name__ == '__main__':
    app.run(debug=True)