class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def check_answer(self, u_ans, c_question):
        if u_ans == c_question.lower():
            self.score += 1
            print("You got it right")
        else:
            print(f"That's wrong")
        print(f"The correct answer was: {c_question}")
        print(f"Your current score is {self.score}/{self.question_number}\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ask_user = input(f"Q.{self.question_number}: {current_question.text}"
                         f" True or False\t").lower()
        correct_answer = current_question.answer
        self.check_answer(u_ans=ask_user, c_question=correct_answer)

    def still_has_question(self) -> bool:
        return self.question_number < len(self.question_list)
