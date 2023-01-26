class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.live = 5
        self.start_game = "yes"

    def still_have_question(self):

        if self.question_number < len(self.question_list) and self.live > 0:
            return True
        else:

            return False

    def next_question(self):

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number} and you {self.live} chances left")
            if self.question_number == len(self.question_list) and self.live > 0:
                print("")
                print("Congratulation! You complete the Quiz successfully")
        else:
            self.live -= 1
            print("You are wrong!")
            print(f"Your current score is {self.score}/{self.question_number} You have {self.live} tries left")
            if self.live == 0:
                print("Its pity! You have tried your best! There is no lives left")




