import eel
from src.login.login import check_login
from src.stats import leetcode, leaderboards
from src.askgemini import askgemini, geministats
import sqlite3

eel.init('web')

signed_in = None

@eel.expose
def login(username, password):
    myconn = sqlite3.connect('prosync.db')
    cur = myconn.cursor()
    r = cur.execute("SELECT username, password, leetcodeid FROM prosync WHERE username = ? AND password = ?", (username, password))
    res = r.fetchone()
    if res:
        cur.execute(f"INSERT INTO signed_in VALUES('{res[2]}')")
        signed_in = res[2]
        return True
    else:
        return False


@eel.expose
def signup(username, password, leetcodeid):
    myconn = sqlite3.connect('prosync.db')
    cur = myconn.cursor()
    r = cur.execute("SELECT username FROM prosync WHERE username = ?", (username,))
    if r.fetchone():
        return False
    else:
        cur.execute("INSERT INTO prosync (username, password, leetcodeid) VALUES (?, ?, ?)", (username, password, leetcodeid))
        myconn.commit()
        return True


@eel.expose
def redirect_to_home():
    eel.show('home.html')

@eel.expose
def askgemini_form(question):
    return askgemini.processQuestion(question)


@eel.expose
def geministats(easy, medium, hard, acceptance, submission):
    return geministats.processstats(easy, medium, hard, acceptance, submission)


@eel.expose
def retrieve_data():
    return leetcode.Leetcode(signed_in)


@eel.expose
def retrieve_leaderboard():
    return leaderboards.sorting()


if __name__ == "__main__":
    eel.start('signin.html', size=(800, 700))
