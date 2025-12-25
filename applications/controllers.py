from main import app
from flask import render_template

from static.variableFiles.variables import client_name, client_bio, showcase_type, showcaseInfo, credentialInfo, copyright_year_range

@app.route('/')
@app.route('/myself')
def myself():
    return render_template("myself.html", client_name=client_name, active1="active", client_bio=client_bio, showcase_type=showcase_type , title_showcase1=showcaseInfo[0][0], info_showcase1=showcaseInfo[0][1], link_showcase1=showcaseInfo[0][2], title_showcase2=showcaseInfo[1][0], info_showcase2=showcaseInfo[1][1], link_showcase2=showcaseInfo[1][2], title_showcase3=showcaseInfo[2][0], info_showcase3=showcaseInfo[2][1], link_showcase3=showcaseInfo[2][2], title_credential1=credentialInfo[0][0], link_credential1=credentialInfo[0][1], title_credential2=credentialInfo[1][0], link_credential2=credentialInfo[1][1], title_credential3=credentialInfo[2][0], link_credential3=credentialInfo[2][1], copyright_year_range=copyright_year_range)

@app.route('/services')
def services():
    return render_template("services.html", client_name=client_name, active2="active")

@app.route('/contact')
def contact():
    return render_template("contact.html", client_name=client_name, active3="active")








