class QuizBrain:

    def __init__(self,quiz_list):
        self.question_number = 0
        self.question_list = quiz_list

    def next_question(self):
        cur_question = self.question_list[self.question_number]
        self.question_list[cur_question["text"]]
        user_guess = input(cur_question)
        self.question_number +=1
        return user_guess == cur_question["answer"]