import requests
import json


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


def submit():
    # TODO: Submission to GenAI
    pass