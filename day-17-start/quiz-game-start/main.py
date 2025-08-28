from question_model import Question
from data import question_data

question_bank = []

for item in question_data:
    entry = Question(item['text'],item['answer'])
    question_bank.append(entry)