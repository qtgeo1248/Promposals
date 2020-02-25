import os, sqlite3, calendar
from flask import Flask, render_template, request, session, redirect, url_for, flash

DB_FILE = "dates.db"
noschool = [3190, 3191, 3200, 3201, 5210, 5211, 5250, 5251, 6040, 6041,
            4090, 4091, 4100, 4101, 4130, 4131, 4140, 4141, 4150, 4151, 4160, 4161, 4170, 4171]

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

def genDates(list):
    month = 3
    day = 2
    for i in range(15):
        for j in range(5):
            for k in range(2):
                cur = ""
                cur += str(month)
                d = day + j
                if (d // 10 == 0):
                    cur += "0"
                cur += str(d)
                cur += str(k)
                if int(cur) not in noschool:
                    list.append(int(cur))
        day += 7
        if (day >= 31) and (month % 2 == 1):
            day -= 31
            month += 1
        if (day >= 30) and (month % 2 == 0):
            day -= 30
            month += 1

def remDates(list):
    command = "SELECT date FROM dates;"
    out = exec(command)
    thingy = out.fetchall()
    allChosen = []
    for item in thingy:
        if str(item) not in allChosen:
            allChosen.append(str(item)[1:-2])
    for item in allChosen:
        if (int(item) in list):
            list.remove(int(item))

def convertDbToStr(dbdate):
    days = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
    month = dbdate // 1000
    day = (dbdate // 10) % 100
    time = dbdate % 10
    eyes = ""
    eyes += " " + str(month) + "/" + str(day) + "/2020 "
    eyes += days[calendar.weekday(2020, month, day)]
    if time == 0:
        eyes += " 4:00 PM"
    else:
        eyes += " 4:30 PM"
    return eyes
