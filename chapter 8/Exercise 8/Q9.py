"""
9. Write a simple quiz game that has a list of ten questions and a list of answers to those questions.
The game should give the player four randomly selected questions to answer. It should
ask the questions one-by-one, and tell the player whether they got the question right or
wrong. At the end it should print out how many out of four they got right.
"""
from random import *

questions = [
    "1 + 5 = ",
    "2 + 1 = ",
    "1 + 1 = ",
    "2 + 2 = ",
    "0 + 5 = ",
    "1 + 9 = "
]
answers = [6, 3, 2, 4, 5, 10]

quiz = sample(questions, 4)


for question in quiz:
    answer = eval(input(question))
    if answer == answers[questions.index(question)]:
        print("Right")
    else:
        print("Wrong")








