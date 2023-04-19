from question_model import Question
from data1 import question_data
from quiz_brain import QuizBrain

question_bank = []
for _ in question_data:
    # text, answer = _.items()
    question_text = _['question']
    question_answer = _['correct_answer']
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

