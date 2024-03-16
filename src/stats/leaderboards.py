import sqlite3 as sql
from leetcode import Leetcode

con = sql.connect('prosync.db')


# CHeck stats of one user
def check_stats(user):
    cur = con.cursor()
    cur.execute("SELECT * FROM prosync WHERE username = ?", (user,))
    r = Leetcode(str(cur.fetchone()[2]))
    con.close()
    return r


if __name__ == "__main__":
    print(check_stats("nilay"))