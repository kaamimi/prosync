import requests
import json

r = requests.get("https://db1.kamalesh2419.workers.dev/login")
res = json.loads(r.text)


def get_login():
    username = []
    hash = []
    leetuser = []
    for d in res:
        username.append(d["name"])
        hash.append(d["hash"])
        leetuser.append(d["leetuser"])
    return username, hash, leetuser


def check_login(username, password):
    user, hash, _ = get_login()
    if username in user and password in hash:
        return True
    else:
        return False