class QuizBrain:

    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1

        user_answer = ""
        # Repeat input prompt until valid input is given
        while user_answer.lower() not in ["true", "false"]:
            user_answer = input(
                f"Q.{self.question_num}: {current_question.text} (True/False): "
            )
            if user_answer.lower() not in ["true", "false"]:
                print("Invalid input. Please type True or False.")

        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got the correct answer!")
            self.score += 1
        else:
            print("Your answer is incorrect!")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is: {self.score} / {self.question_num}")
        print("\n")
