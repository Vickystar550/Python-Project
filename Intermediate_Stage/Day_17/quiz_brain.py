class QuizBrain:
    def __init__(self, q_list):
        self.q_item = None
        self.question_number = 0
        self.question_list = q_list
        self.correct_question = 0
        self.wrong_question = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f"\nYou've completed this quiz. "
                  f"You got {self.correct_question} questions correct, and {self.wrong_question} wrong")
            return False

    def next_question(self):
        # retrieve the question at the current question number:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number}: {current_question.text}. (true/false)?\n")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.title() == correct_answer:
            self.correct_question += 1
            print(f"\nYou got it right\nThe correct answer was: {correct_answer}.\nYour correct "
                  f"score is {self.correct_question}/{self.question_number}")
        else:
            self.wrong_question += 1
            print(f"\nYou got it wrong\nThe correct answer was: {correct_answer}")
