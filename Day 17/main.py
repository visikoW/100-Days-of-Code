from question_model import Question
from quiz_brain import QuizzBrain
from data import question_data

question_bank = []

for x in question_data:
    question_text = x['question']
    question_answer = x['correct_answer']

    new_question = Question(question_text, question_answer)

    question_bank.append(new_question)

quizz = QuizzBrain(question_bank)

while quizz.still_has_question():
    quizz.next_question()

print('You\'ve completed the quiz')
print(f'Your final score was: {quizz.score}/{quizz.question_number}')
