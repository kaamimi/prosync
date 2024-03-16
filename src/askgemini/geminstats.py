import askgemini.respond_to_question as response_to_question

def get_gemini_stats():
    return response_to_question("What is my LeetCode stats?")

print(get_gemini_stats())