import db, os, sqlite3
from flask import Flask, render_template, request, session, redirect, url_for, flash

list = []
image = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/237/revolving-hearts_1f49e.png"

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def index():
    db.genDates(list)
    db.remDates(list)
    return render_template("landing.html", happy = list, img = image)

@app.route("/date")
def addDate():
    happy = str(request.args["dat"])
    if db.authenticate(happy):
        command = "INSERT INTO dates (id, date) VALUES (" + request.args["ID"] + ", '" + request.args["dat"] + "');"
        db.exec(command)
        return render_template("out.html", selectedDate = db.convertDbToStr(int(request.args["dat"])), img = image)
    else:
        db.genDates(list)
        db.remDates(list)
        return render_template("landing.html", error = "Unfortunately, your date is already chosen :(", img = image, error2 = "Please choose a different date.", happy = list)

@app.route("/checking")
def renderDate():
    return render_template("checker.html")

@app.route("/checked")
def checkDate():
    osis = int(request.args["ID"])
    registered = db.check(osis)
    if len(registered) == 0:
        return render_template("checker.html", all = registered, error = "Unfortunately, you have not signed up for a prom date yet")
    else:
        return render_template("checker.html", all = registered, id = osis)

if __name__ == "__main__":
    db.setup()
    app.debug = True
    app.run()
