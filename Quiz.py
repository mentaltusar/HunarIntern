import requests
import html


class Question:
    def __init__(self, prompt, correct_answer, options):
        self.prompt = prompt
        self.correct_answer = correct_answer
        self.options = options


def fetch_questions(amount=5, category=None, difficulty=None):
    url = "https://opentdb.com/api.php"
    params = {
        "amount": amount,
        "type": "multiple"
    }
    if category:
        params["category"] = category
    if difficulty:
        params["difficulty"] = difficulty

    response = requests.get(url, params=params)
    data = response.json()

    questions = []
    for item in data["results"]:
        prompt = html.unescape(item["question"])
        correct_answer = html.unescape(item["correct_answer"])
        options = [html.unescape(option) for option in item["incorrect_answers"]]
        options.append(correct_answer)
        options.sort()
        questions.append(Question(prompt, correct_answer, options))

    return questions


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        for i, option in enumerate(question.options, 1):
            print(f"{i}. {option}")
        answer = input("Enter the number of your answer: ")
        if question.options[int(answer) - 1].lower() == question.correct_answer.lower():
            score += 1
    print(f"You got {score} out of {len(questions)} correct!")


def main():
    amount = int(input("How many questions would you like? "))
    cat = None
    difficulty = input("Enter difficulty (easy, medium, hard): ")

    questions = fetch_questions(amount, cat, difficulty)
    run_quiz(questions)


if __name__ == "__main__":
    main()
