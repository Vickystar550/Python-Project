import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for q in data.question_data:
    question_object = Question(q)
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the Quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
