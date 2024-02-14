class Question:
    def __init__(self, text, choices, correct_answer):
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer
    def check_answer(self, answer):
        return answer.lower() == self.correct_answer.lower()
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.total_questions = len(questions)
    def take_quiz(self):
        print("Welcome to the Quiz Game!")
        print("Rules: Enter the number corresponding to your answer.")
        for i, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {i}: {question.text}")
            for j, choice in enumerate(question.choices, start=1):
                print(f"{j}. {choice}")
            answer = input("Enter your answer: ")
            if question.check_answer(answer):
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer is: {question.correct_answer}")
    def display_score(self):
        print(f"\nYou scored {self.score} out of {self.total_questions}")
def main():
    q1 = Question("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "Paris")
    q2 = Question("Which planet is known as the Red Planet?", ["Jupiter", "Mars", "Saturn", "Venus"], "Mars")
    q3 = Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "Blue Whale")
    quiz = Quiz([q1, q2, q3])
    quiz.take_quiz()
    quiz.display_score()
if __name__ == "__main__":
    main()
