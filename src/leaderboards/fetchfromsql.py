import sqlite3
import pathlib
from login.login import get_login


# Create a database if it doesn't exist
if not pathlib.Path('leaderboards.db').is_file():
    conn = sqlite3.connect('leaderboards.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE leaderboards
                    (leetuser varchar(255), score integer)''')
    conn.commit()
    conn.close()


def checkifexists(leetuser):
    _, _, leetusr = get_login()
    if leetusr == leetuser:
        return True
    return False


def get_leaderboards(leetuser):
    if not checkifexists(leetuser):
        return "User not found"
    conn = sqlite3.connect('leaderboards.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM leaderboards WHERE leetuser = '{leetuser}'")
    res = c.fetchall()
    conn.close()
    return res