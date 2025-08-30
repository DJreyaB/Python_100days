from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = item["text"]
    response = item["answer"]
    entry = Question(question,response)
    question_bank.append(entry)

quiz = QuizBrain(question_bank)
print(quiz.question_list)