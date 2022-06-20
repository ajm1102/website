from flask import Flask, render_template, request, redirect, url_for, session
from functions import upload_spaces
from serverConfig import flasksecretkey
app = Flask(__name__)
rendered = False
app.secret_key = flasksecretkey

@app.route('/', methods=['POST', 'GET'])
def Simulation():
    if request.method == "POST":
        Xcords = request.form['Xcords']
        Ycords = request.form['Ycords']
        session["Xcords"] = Xcords
        session["Ycords"] = Ycords
        session['rendered'] = False
        return redirect(url_for("results"))
    else:
        return render_template("index.html")


@app.route('/results')
def results():
    if "Xcords" in session and "Ycords" in session and session['rendered'] == False:
        session['rendered'] = True
        upload_spaces(session["Xcords"], session["Ycords"])
        return render_template('display.html', xcord=session["Xcords"], ycord=session["Ycords"])
    elif "Xcords" in session and "Ycords" in session and session['rendered'] == True:
        return render_template('display.html', xcord=session["Xcords"], ycord=session["Ycords"])
    else:
        return redirect(url_for('Simulation'))


if __name__ == '__main__':
    app.run(debug=True)
