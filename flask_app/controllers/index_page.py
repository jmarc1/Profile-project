from flask_app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register_user')
def register_user():
    return render_template("/login_register.html")