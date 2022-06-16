from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "hello"

@app.route('/', methods=['POST', 'GET'])
def Simulation():
    if request.method == "POST":
        user = request.form['nm']
        session["user"] = user
        return redirect(url_for("results"))
    else:
        return render_template("index.html")


@app.route('/results')
def results():
    if "user" in session:
        user = session["user"]
        user = user + 'XYZ'
        return render_template('display.html', content=user)
    else:
        return redirect(url_for('Simulation'))



if __name__ == '__main__':
    app.run(debug=True)
