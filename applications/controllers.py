from main import app
from flask import render_template, request, redirect


from static.variableFiles.variables import client_name, client_bio, showcase_type, showcaseInfo, credentialInfo, copyright_year_range, serviceList

@app.route('/')
@app.route('/myself')
def myself():
    return render_template("myself.html", client_name=client_name, active1="active", client_bio=client_bio, showcase_type=showcase_type , title_showcase1=showcaseInfo[0][0], info_showcase1=showcaseInfo[0][1], link_showcase1=showcaseInfo[0][2], title_showcase2=showcaseInfo[1][0], info_showcase2=showcaseInfo[1][1], link_showcase2=showcaseInfo[1][2], title_showcase3=showcaseInfo[2][0], info_showcase3=showcaseInfo[2][1], link_showcase3=showcaseInfo[2][2], title_credential1=credentialInfo[0][0], link_credential1=credentialInfo[0][1], title_credential2=credentialInfo[1][0], link_credential2=credentialInfo[1][1], title_credential3=credentialInfo[2][0], link_credential3=credentialInfo[2][1], copyright_year_range=copyright_year_range)

@app.route('/services', methods=["GET", "POST"])
def services():
    if request.method == 'GET':
        return render_template("services.html", client_name=client_name, active2="active", copyright_year_range=copyright_year_range, serviceTitle1=serviceList[0][0], serviceDesc1=serviceList[0][1], serviceTitle2=serviceList[1][0], serviceDesc2=serviceList[1][1], serviceTitle3=serviceList[2][0], serviceDesc3=serviceList[2][1], serviceTitle4=serviceList[3][0], serviceDesc4=serviceList[3][1])
    elif request.method == 'POST':
        service = int(request.form.get('service'))
        if (service > 0) and ((service < len(serviceList)) or (service == len(serviceList)) ):
            return redirect("/services/{id}".format(id=service), code=302)
        else:
            return redirect("/404", code=302)


@app.route('/services/<int:id>', methods=["GET", "POST"])
def service(id):
    return render_template("servicesDir/bookService.html", client_name=client_name, active2="active", copyright_year_range=copyright_year_range)

@app.route('/contact')
def contact():
    return render_template("contact.html", client_name=client_name, active3="active", copyright_year_range=copyright_year_range)

@app.errorhandler(404)
def notFound(error):
    return render_template("404.html", client_name=client_name, active2="active", copyright_year_range=copyright_year_range), 404






