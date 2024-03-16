import requests
import json

r = requests.get("https://db1.kamalesh2419.workers.dev/login")
res = json.loads(r.text)


def check_login():
    username = []
    hash = []
    for d in res:
        username.append(d["username"])
        hash.append(d["hash"])
    return username, hash