class QuizBrain:

    def __init__(self,quiz_list):
        self.question_number = 0
        self.question_list = quiz_list


    def still_has_questions(self):
        return self.question_number < len(self.question_list)    
    
    def next_question(self):
        while self.still_has_questions():
            self.question_number
            self.question_list
            cur_question = self.question_list[self.question_number]
            self.question_number +=1
            cur_question.text
            self.question_list[cur_question.text]
            user_guess = input(f"Q.{self.question_number} {cur_question} (True/False)")
            return user_guess == cur_question["answer"]
    