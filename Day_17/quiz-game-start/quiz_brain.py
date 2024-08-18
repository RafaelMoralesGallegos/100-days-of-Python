class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(user_answer, question.answer)

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, u_answer, q_answer):
        if u_answer.lower() == q_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print("That is Wrong.")

        print(f"The correct answer was: {q_answer}.")
        print(f"Your score is {self.score}/{self.question_number}.")
        print("\n")

    def quiz_end(self):
        print("You've completed the quiz.")
        print(f"Your final score is: {self.score}/{self.question_number}.")
