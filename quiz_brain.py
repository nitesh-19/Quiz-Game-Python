class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def get_question(self, question_number):
        return self.question_list[question_number].text

    def check_answer(self, response):
        if response.lower() == self.question_list[self.question_number].answer.lower():
            return True
        else:
            return False

    def still_has_questions(self, question_bank):
        if self.question_number == len(question_bank):
            return False
        else:
            return True

    def ask_question(self):
        response = input(
            f"Q.{self.question_number + 1}: {self.get_question(question_number=self.question_number)} (True/False)?: ")
        if self.check_answer(response):
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {self.question_list[self.question_number].answer}")
        print(f"Your current score is {self.score}/{self.question_number + 1}")
        self.question_number += 1
        return response
