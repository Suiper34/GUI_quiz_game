
import html
from random import shuffle

import requests

quiz_parameters = {
    "amount": 15,
    "category": 18,
    "difficulty": "hard",
    "type": "multiple",
}

quiz_response = requests.get(
    url='https://opentdb.com/api.php', params=quiz_parameters)
quiz_response.raise_for_status()


ques_ans_dataa = quiz_response.json()['results']

# add correct ans to incorrect to get full quiz answer options
for a_dict in ques_ans_dataa:
    (a_dict['incorrect_answers']).append(a_dict['correct_answer'])
    shuffle(a_dict['incorrect_answers'])

    # html unescape to change html entites back to original format
    a_dict['question'] = html.unescape(a_dict['question'])
    a_dict['incorrect_answer'] = [html.unescape(
        ans) for ans in a_dict['incorrect_answers']]

ques_ans_data = ques_ans_dataa
