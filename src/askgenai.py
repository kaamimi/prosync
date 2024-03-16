# Python code

import eel
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyDh3GF-duFIKtzDPrsgHQijUIX03K0I8OQ"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")

eel.init('web')  
def checkwhethervalid(question):
    response = model.generate_content(question)
    return response.text

def respond_to_question(question):
    response = model.generate_content(question)
    return response.text

@eel.expose
def processQuestion(question):
    response = respond_to_question(question)
    valid_response = checkwhethervalid("check whether the following prompt is related to coding or is appropriate for a student and return either 'true' or 'false' single word reply, the message is: " + response)
    if (valid_response.strip().lower() == "true"):
        return response
    else:
        return "Enter an appropriate message related to programming"

eel.start('stats.html', size=(600, 600))
