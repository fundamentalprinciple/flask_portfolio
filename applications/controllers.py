from main import app
from flask import render_template

from variables import client_name

@app.route('/')
@app.route('/myself')
def myself():
    return render_template("myself.html", client_name=client_name, active1="active")

@app.route('/services')
def services():
    return render_template("services.html", client_name=client_name, active2="active")

@app.route('/contact')
def contact():
    return render_template("contact.html", client_name=client_name, active3="active")








