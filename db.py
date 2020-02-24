import os, sqlite3
from flask import Flask, render_template, request, session, redirect, url_for, flash

DB_FILE = "dates.db"

def setup():
    command = "CREATE TABLE IF NOT EXISTS dates (id INT, date INT);"
    exec(command)

def exec(cmd):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    output = c.execute(cmd)
    db.commit()
    return output

def authenticate(date):
    command = "SELECT date FROM dates WHERE '" + date + "' = date;"
    out = exec(command)
    thingy = out.fetchone()
    if thingy is None:
        return True
    return False
