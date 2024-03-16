import eel
import google.generativeai as genai
import requests
import json

def Leetcode(user):
    try:
        r = requests.get(f"https://leetcode-stats-api.herokuapp.com/{user}")
        res = json.loads(r.text)

        if res["status"] == "success" and res["message"] == "retrieved":
            Easy = res["easySolved"]
            Medium = res["mediumSolved"]
            Hard = res["hardSolved"]
            Acceptance = res["acceptanceRate"]
            SubmissionCalendar = res["submissionCalendar"]

            return Easy, Medium, Hard, Acceptance, SubmissionCalendar
        else:
            return None  
    except Exception as e:
        print(f"Error: {e}")
        return None

leetid="kaamimi"
result = Leetcode("kaamimi")
if result:
    easy, medium, hard, acceptance, submission = result
    print(easy)  # Easy
else:
    print("User does not exist or API call failed.")



GOOGLE_API_KEY = "AIzaSyDh3GF-duFIKtzDPrsgHQijUIX03K0I8OQ"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")

eel.init('../web/pages')  

def respond_to_question(question):
    response = model.generate_content(question)
    return response.text
#add the stats to the html 
@eel.expose
def processstats():
    response = respond_to_question('can you give me a brief analysis of a user with the following leetcode stats: easy:'+str(easy) +"medium:"+str(medium)+"hard:"+str(hard)+"acceptance:"+str(acceptance)+"submissioncalender"+str(submission)+"in around 300 words")
    return response

eel.start('statsfinal.html', size=(600, 600))
