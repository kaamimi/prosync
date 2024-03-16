import eel
from src.login.login import check_login
from src.stats import leetcode
import sqlite3

eel.init('web')


@eel.expose
def Leetcode():
    return leetcode.Leetcode("kaamimi")

@eel.expose
def login(username, password):
    myconn = sqlite3.connect('prosync.db')
    cur = myconn.cursor()
    r = cur.execute("SELECT * FROM prosync WHERE username = ? AND password = ?", (username, password))
    if r.fetchone():
        return True
    else:
        return False


@eel.expose
def redirect_to_home():
    eel.show('home.html')


if __name__ == "__main__":
    eel.start('signin.html', size=(700, 500))
    print(Leetcode())
