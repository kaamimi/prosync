import google.generativeai as genai
import requests, json

GOOGLE_API_KEY = "AIzaSyDh3GF-duFIKtzDPrsgHQijUIX03K0I8OQ"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def Leetcode(user):
    r = requests.get(f"https://leetcode-stats-api.herokuapp.com/{user}")
    res = json.loads(r.text)

    if res["status"] == "success" and res["message"] == "retrieved":
        Easy = res["easySolved"]
        Medium = res["mediumSolved"]
        Hard = res["hardSolved"]
        Acceptance = res["acceptanceRate"]
        SubmissionCalendar = res["submissionCalendar"]
    
    return Easy, Medium, Hard, Acceptance, SubmissionCalendar


def respond_to_question(question):
    response = model.generate_content(question)
    return response.text


def processstats(easy, medium, hard, acceptance, submission):
    response = respond_to_question('can you give me a brief analysis of a user with the following leetcode stats: easy:'+str(easy) +"medium:"+str(medium)+"hard:"+str(hard)+"acceptance:"+str(acceptance)+"submissioncalender"+str(submission)+"in around 300 words")
    return response


def give_stats(user):
    x = Leetcode(user)
    response = processstats(x[0], x[1], x[2], x[3], x[4])
    return response