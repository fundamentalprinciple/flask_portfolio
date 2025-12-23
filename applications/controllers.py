from main import app
from flask import render_template

from static.variableFiles.variables import client_name, client_bio, projectInfo

@app.route('/')
@app.route('/myself')
def myself():
    return render_template("myself.html", client_name=client_name, active1="active", client_bio=client_bio, link_project1=projectInfo[0][1], info_project1=projectInfo[0][0])

@app.route('/services')
def services():
    return render_template("services.html", client_name=client_name, active2="active")

@app.route('/contact')
def contact():
    return render_template("contact.html", client_name=client_name, active3="active")








