import eel
from src.login.login import check_login

eel.init('web')

signed_in = False

@eel.expose
def login(username, password):
    if check_login(username, password):
        return True
    else:
        return False

@eel.expose
def get_signin_status():
    return signed_in

def open_page():
    if signed_in:
        eel.start('home.html')
    else:
        eel.start('signin.html')

# Start the app
if __name__ == "__main__":
    open_page()
