import google.generativeai as genai
from leetcode import Leetcode

GOOGLE_API_KEY = "AIzaSyDh3GF-duFIKtzDPrsgHQijUIX03K0I8OQ"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")


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