print("---------simple quiz-----------")



class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def display_method(self):
        print("\n" + self.question)
        for i, option in enumerate(self.options, start=1):
            print(i, option)

    def check_answer(self, user_input):
        return user_input == self.answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start_quiz(self):
        ready = input("Are you ready for the quiz? (yes/no): ")

        if ready.lower() != "yes":
            print("Okay, exiting quiz.")
            return

        print("\nStarting Quiz...\n")

        for question in self.questions:
            while True:  
                question.display_method()

                try:
                    user_input = int(input("Enter option number: "))
                except ValueError:
                    print("Invalid input! Enter a number.\n")
                    continue

                if question.check_answer(user_input):
                    print("Correct!")
                    self.score += 1
                    break  
                else:
                    print("Wrong! Try again.\n")

        print("\nFinal Score:", self.score)
q1 = Question(
    "What is the capital of India?",
    ["Mumbai", "Delhi", "Kolkata", "Chennai"],
    2
)

q2 = Question(
    "Which language is used for Python programming?",
    ["Java", "English", "Python", "C++"],
    3
)

q3 = Question(
    "What is 5 + 3?",
    ["5", "8", "10", "6"],
    2
)

q4 = Question(
    "Which keyword is used to define a class in Python?",
    ["function", "define", "class", "object"],
    3
)

q5 = Question(
    "Which data type is used to store True/False?",
    ["int", "str", "bool", "float"],
    3
)

questions = [q1, q2, q3, q4, q5]
quiz = Quiz(questions)
quiz.start_quiz()            
