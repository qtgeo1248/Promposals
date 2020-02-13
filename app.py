import os
from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route('/')
def index():
    return render_template("landing.html")

@app.route("/date")
def addDate():
    print(request.args["dat"])
    return render_template("yourDate.html", selectedDate = request.args["dat"])


if __name__ == "__main__":
    app.debug = True
    app.run()
