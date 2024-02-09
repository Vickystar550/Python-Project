from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface


# making the question from question_data a Question class object
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


# make a QuizBrain class with the list containing the question object i.e., question_bank
quiz = QuizBrain(question_bank)

# create an interface object from the QuizInterface class which takes a QuizBrain object -> quiz
interface = QuizInterface(quiz)


