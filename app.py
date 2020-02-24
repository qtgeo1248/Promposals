import db, os, sqlite3
from flask import Flask, render_template, request, session, redirect, url_for, flash

list = [3020, 3021]

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def index():
    return render_template("landing.html")

@app.route("/date")
def addDate():
    #if happy == "":
    #    return render_template("landing.html", error = "You have to pick a date ;)")
    if db.authenticate(happy):
        command = "INSERT INTO dates (id, date) VALUES (" + request.args["ID"] + ", '" + request.args["dat"] + "');"
        db.exec(command)
        print(request.args["dat"])
        return render_template("yourDate.html", selectedDate = request.args["dat"])
    else:
        return render_template("landing.html", error = "Unfortunately, your date is already chosen :(", error2 = "Please choose a different date.")

if __name__ == "__main__":
    db.setup()
    app.debug = True
    app.run()
