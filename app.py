import eel

# Set web files folder
eel.init('web')

@eel.expose
def login(username, password):
    if username == "user" and password == "password":
        return True
    else:
        return False

# Start the app
eel.start('home.html')
