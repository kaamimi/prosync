import eel
from src.login.login import check_login
from src.stats import leetcode
from src.askgemini import askgenai
import sqlite3

eel.init('web')


@eel.expose
def Leetcode():
    return leetcode.Leetcode("kaamimi")


@eel.expose
def login(username, password):
    myconn = sqlite3.connect('prosync.db')
    cur = myconn.cursor()
    r = cur.execute("SELECT username, password, leetcodeid FROM prosync WHERE username = ? AND password = ?", (username, password))
    res = r.fetchone()
    if res:
        cur.execute(f"INSERT INTO signed_in VALUES('{res[2]}')")
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
def askgemini(question):
    return askgenai.processQuestion(question)


if __name__ == "__main__":
    eel.start('home.html', size=(800, 700))
    print(Leetcode())
