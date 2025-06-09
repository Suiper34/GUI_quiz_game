import tkinter as tk
from tkinter import ttk

import quiz_brain
from question_model import QuestionModel as q_m

GREEN = "#253c23"
OPTION_INDEX = ('a', 'b', 'c', 'd')

ques_ans_data = [
    {
        "type": "multiple",
        "difficulty": "hard",
        "category": "Science: Computers",
        "question": "What vulnerability ranked #1 on the OWASP Top 10 in 2013?",
        "correct_answer": "Injection",
        "options": [
                "Broken Authentication",
                "Cross-Site Scripting",
                "Injection",
                "Insecure Direct Object References"
        ]
    },
    {
        "type": "multiple",
        "difficulty": "hard",
        "category": "Science: Computers",
        "question": "Who is the founder of Palantir?",
        "correct_answer": "Peter Thiel",
        "options": [
                "Peter Thiel",
                "Mark Zuckerberg",
                "Marc Benioff",
                "Jack Dorsey"
        ]
    },]


questions_answers_bank = []
question_data = ques_ans_data

for data in question_data:
    ques_model = q_m(data["question"],
                     data["correct_answer"], data["options"])

    questions_answers_bank.append(ques_model)
ques_structure = questions_answers_bank


class Interface:
    def __init__(self, questions_data_list: list):
        self.initial_score = 0
        self.ques_data_list = questions_data_list
        self.ques_data_index = 0
        self.rootscreen = tk.Tk()
        self.rootscreen.title('MCQ Quiz Game')
        self.rootscreen.maxsize(750, 750)
        self.rootscreen.configure(bg=GREEN)

        self.style = ttk.Style()
        self.main_frame = ttk.Frame(
            self.rootscreen, height=700, width=700, padding=30)
        self.main_frame.grid()

        self.style.configure('TFrame', background=GREEN)
        score_frame = ttk.Frame(self.main_frame, padding=20,)
        score_frame.grid(column=1, row=0)

        self.style.configure('TLabel', font=(
            'Times new roman', 13), background=GREEN, foreground='white')

        # score section
        self.score = ttk.Label(score_frame, text='score:', padding=3)
        self.score.grid(column=0, row=0)

        self.score_point = ttk.Label(score_frame, text=self.initial_score)
        self.score_point.grid(column=1, row=0)

        # canvas and quiz question structure section
        self.canvas = tk.Canvas(self.main_frame, highlightthickness=0,
                                height=250, width=350, bg='white')
        self.quiz_question = self.canvas.create_text(175, 125, text=f'{self.ques_data_list[self.ques_data_index].ques}',
                                                     font=('Times new roman', 14), width=300, fill=GREEN)
        self.canvas.grid(column=0, row=1, columnspan=2)

        # ques options section:
        answers_frame = ttk.Frame(self.main_frame, padding=20)
        answers_frame.grid(column=0, row=2)

        self.options_labels = []

        for i, option in enumerate(self.ques_data_list[self.ques_data_index].options):
            option_indexs = ttk.Label(
                answers_frame, text=f'{OPTION_INDEX[i]}.')
            option_indexs.grid(column=0, row=i, padx=10)
            options = ttk.Label(answers_frame, text=option)
            options.grid(column=1, row=i)
            self.options_labels.append(options)

        # user answer section
        user_answer_frame = ttk.Frame(self.main_frame, padding=10)
        user_answer_frame.grid(column=0, row=4, columnspan=2)

        label = ttk.Label(
            user_answer_frame, text='Enter the correct answer below ',)
        label.grid(column=0, row=0, pady=15, columnspan=2)

        self.answer_input = ttk.Entry(
            user_answer_frame, font=('Times new roman', 14))
        self.answer_input.focus()
        self.answer_input.grid(column=0, row=1, padx=10,)

        self.check_button = ttk.Button(
            user_answer_frame, text='Check Answer', command=self.check_command)
        self.check_button.grid(column=1, row=1)

        self.rootscreen.mainloop()

    def check_command(self):
        if self.ques_data_index < len(self.ques_data_list):
            user_ans = self.answer_input.get()  # get hold of user input
            if user_ans.lower() == (self.ques_data_list[self.ques_data_index].ans).lower():
                self.initial_score += 1
                self.score_point.configure(text=self.initial_score)

            self.ques_data_index += 1
            self.next_question()
        self.answer_input.delete(0, len(user_ans))

    def next_question(self):
        if self.ques_data_index < len(self.ques_data_list):
            self.canvas.itemconfigure(
                self.quiz_question, text=self.ques_data_list[self.ques_data_index].ques)

            for i in range(len(self.ques_data_list[self.ques_data_index].options)):
                self.options_labels[i].configure(
                    text=self.ques_data_list[self.ques_data_index].options[i])

        else:
            self.score.configure(text='Total Score:')
            self.score_point.configure(
                text=f'{self.initial_score}/{len(self.ques_data_list)}')


Interface(ques_structure)
