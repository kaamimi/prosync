import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyDh3GF-duFIKtzDPrsgHQijUIX03K0I8OQ"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def respond_to_question(question):
    response = model.generate_content(question)
    return response.text

# Prompt this to use user's LeetCode stats and give an analysis of your performance.