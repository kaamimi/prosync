import requests
import json


class LeetCode:
    def __init__(self, user):
        Easy = 0
        Medium = 0
        Hard = 0
        Acceptance = None
        SubmissionCalendar = None

        r = requests.get(f"https://leetcode-stats-api.herokuapp.com/{user}")
        res = json.loads(r.text)
    
        if res["status"] == "success" and res["message"] == "retrieved":
            self.Easy = res["easySolved"]
            self.Medium = res["mediumSolved"]
            self.Hard = res["hardSolved"]
            self.Acceptance = res["acceptanceRate"]
            self.SubmissionCalendar = res["submissionCalendar"]

    def submit(self):
        # TODO: Submission to GenAI
        pass


if __name__ == "__main__":
    k = LeetCode("kaamimi")