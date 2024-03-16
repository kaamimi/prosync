import sqlite3 as sql
import requests, json

con = sql.connect('prosync.db')


def Leetcode(user):
    r = requests.get(f"https://leetcode-stats-api.herokuapp.com/{user}")
    res = json.loads(r.text)

    if res["status"] == "success" and res["message"] == "retrieved":
        Easy = res["easySolved"]
        Medium = res["mediumSolved"]
        Hard = res["hardSolved"]
        Acceptance = res["acceptanceRate"]
        SubmissionCalendar = res["submissionCalendar"]
    
    return Easy, Medium, Hard, Acceptance, SubmissionCalendar



# Check stats of one user
def check_stats(user):
    cur = con.cursor()
    cur.execute("SELECT * FROM prosync WHERE username = ?", (user,))
    r = Leetcode(str(cur.fetchone()[2]))
    con.close()
    return r


def logged_in():
    cur = con.cursor()
    cur.execute("SELECT * FROM signed_in")
    r = cur.fetchall()
    con.close()
    return r


def sorting():
    cur = con.cursor()
    cur.execute("SELECT leetcodeid FROM prosync")
    r = [i[0] for i in cur.fetchall()]
    res = {}
    for i in r:
        e, m, h, _, _ = Leetcode(i)
        res[i] = e + m*2 + h*3

    con.close()
    return res