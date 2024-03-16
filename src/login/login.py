import requests
import json

r = requests.get("https://db1.kamalesh2419.workers.dev/login")
res = json.loads(r.text)


def get_login():
    username = []
    hash = []
    for d in res:
        username.append(d["name"])
        hash.append(d["hash"])
    return username, hash


def check_login(username, password):
    user, hash = get_login()
    if username in user and password in hash:
        return True
    else:
        return False

    
if __name__ == "__main__":
    print(check_login("kamalesh", "ANDYANNNAANDYANNA"))