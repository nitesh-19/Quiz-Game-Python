class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list

    def get_question(self, question_number):
        return self.question_list[question_number].text

    def ask_question(self):
        response = input(
            f"Q.{self.question_number + 1}: {self.get_question(question_number=self.question_number)} (True/False)?: ")
        return response
