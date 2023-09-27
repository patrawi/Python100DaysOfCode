"""Quiz Brain"""


from question_model import Question


class QuizBrain:
    def __init__(self, questions):
        quiz_bank = [Question(q["text"], q["answer"]) for q in questions]
        self.questions = quiz_bank
        self.score = 0
        self.total_number_questions = len(questions)
        self.answered_question = 0

    def check_answer(self, answer, correct_answer):
        """check answer"""
        if answer == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.answered_question} \n\n")

    def ask_question(self):
        question = self.questions[self.answered_question]
        answer = input(
            f"Q.{self.answered_question+ 1}: {question.text} (True/False): "
        ).lower()
        self.answered_question += 1
        self.check_answer(answer, question.answer)

    def check_end_of_quiz(self):
        """is_end"""
        return self.total_number_questions == self.answered_question
