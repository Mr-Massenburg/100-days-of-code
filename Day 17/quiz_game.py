# Day 17 | Question game - creating my own classes

from question_model import Question
from data import question_data
# from data_2 import question_data # Line that would be used to swap questions out
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))
    # question_bank.append(Question(item["question"], item["correct_answer"])) # Line would be used to call the  correct keys from the second question set

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
