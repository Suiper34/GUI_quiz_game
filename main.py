
from ques_and_ans import ques_ans_data as q_a_d
from question_model import QuestionModel as q_m
from quiz_ui import QuizInterface

questions_answers_bank = []

question_data = q_a_d

for data in question_data:
    ques_model = q_m(data["question"],
                     data["correct_answer"], data["incorrect_answers"])
    questions_answers_bank.append(ques_model)

QuizInterface(questions_answers_bank)
