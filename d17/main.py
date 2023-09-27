"""Quiz """
from quiz_brain import QuizBrain
from data import question_data


def main():
    """main"""
    quiz_brain = QuizBrain(questions=question_data)
    while not quiz_brain.check_end_of_quiz():
        quiz_brain.ask_question()

    print("You've completed the quiz")
    print(f"You final score was:{quiz_brain.score}/{quiz_brain.answered_question}")


if __name__ == "__main__":
    main()
