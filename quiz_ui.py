import tkinter as tk
from tkinter import ttk

import quiz_brain
from question_model import QuestionModel as q_m

GREEN = "#14ca0b"
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
    def __init__(self, questions_data_list):
        self.initial_score = 0
        self.ques_data_list = questions_data_list
        self.ques_data_index = 0
        self.rootscreen = tk.Tk()
        self.rootscreen.title('MCQ Quiz Game')
        self.rootscreen.maxsize(750, 750)
        self.rootscreen.configure(bg=GREEN)

        self.style = ttk.Style()
        main_frame = ttk.Frame(
            self.rootscreen, height=700, width=700, padding=30)
        main_frame.grid()

        self.style.configure('TFrame', background=GREEN)
        score_frame = ttk.Frame(main_frame, padding=20,)
        score_frame.grid(column=1, row=0)

        self.style.configure('TLabel', font=(
            'Times new roman', 14), background=GREEN)
        score = ttk.Label(score_frame, text='score:', padding=3)
        score.grid(column=0, row=0)

        score_point = ttk.Label(score_frame, text=0)
        score_point.grid(column=1, row=0)

        canvas = tk.Canvas(main_frame, highlightthickness=0,
                           height=300, width=350, bg='white')
        canvas.create_text(175, 150, text=f'{self.ques_data_list[self.ques_data_index].ques}',
                           font=('Times new roman', 14),)
        canvas.grid(column=0, row=1, columnspan=2)

        answers_frame = ttk.Frame(main_frame, padding=20)
        answers_frame.grid(column=0, row=2)

        i = 0

        for option in self.ques_data_list[self.ques_data_index].options:
            option_indexs = ttk.Label(
                answers_frame, text=f'{OPTION_INDEX[i]}.')
            option_indexs.grid(column=0, row=i, padx=10)
            options = ttk.Label(answers_frame, text=option)
            options.grid(column=1, row=i)
            i += 1

        user_answer_frame = ttk.Frame(main_frame, padding=20)
        user_answer_frame.grid(column=0, row=3, columnspan=2)

        answer_input = ttk.Entry(
            user_answer_frame, font=('Times new roman', 14))
        answer_input.focus()
        answer_input.grid(column=0, row=0, padx=10)

        def check_command():
            user_ans = answer_input.get()
            if user_ans.lower() == (self.ques_data_list[self.ques_data_index].ans).lower():
                correct = tk.PhotoImage(file='./images/right.png')
                canva = tk.Canvas(main_frame, height=50, width=50,
                                  background=GREEN, highlightthickness=0)
                canva.create_image(25, 25, image=correct)
                canva.grid(column=0, columnspan=2, row=4, padx=40, pady=15)
            else:
                incorrect = tk.PhotoImage(file='./images/wrong.png')
                canva = tk.Canvas(main_frame, height=50, width=50,
                                  background=GREEN, highlightthickness=0)
                canva.create_image(25, 25, image=incorrect)
                canva.grid(column=0, columnspan=2, row=4, padx=40, pady=15)

        check_button = ttk.Button(
            user_answer_frame, text='Check Answer', command=check_command)
        check_button.grid(column=1, row=0)

        self.rootscreen.mainloop()


Interface(ques_structure)
