class QuizBrain:
    """Act like the quiz model"""
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = self.question_list[self.question_number]

    def still_has_questions(self):
        """Checks if question still exists"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """get the next question after updating the question number"""
        self.question_number += 1
        try:
            self.current_question = self.question_list[self.question_number]
        except IndexError:
            return "No Question"
        else:
            return self.current_question.text

    def check_answer(self, user_answer):
        """check the question answer"""
        if self.still_has_questions():
            correct_answer = self.current_question.answer
            # check if question answer is correct
            if user_answer.lower() == correct_answer.lower():
                self.score += 1    # update score
                return f"Score: {self.score}/{len(self.question_list)}", "correct"
            else:
                return f"Score: {self.score}/{len(self.question_list)}", "incorrect"
        else:
            return f"Score: {self.score}/{len(self.question_list)}", "end"
