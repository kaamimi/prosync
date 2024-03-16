import eel
from src.login.login import check_login
from src.stats import leetcode

eel.init('web')


@eel.expose
def login(username, password):
    if check_login(username, password):
        return True
    else:
        return False


@eel.expose
def redirect_to_home():
    eel.show('home.html')


# Start the app
if __name__ == "__main__":
    eel.start('signin.html', size=(700, 500))
