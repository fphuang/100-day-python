from flask import Flask
import random

app = Flask(__name__)

random_answer = random.randint(1, 10)


@app.get('/')
def guess_number():
    # random_answer = random.randint(1, 10)
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>." \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width='200px'>"


@app.get('/<int:guess>/')
def get_answer(guess):
    print(f'the correct answer is: {random_answer}')
    if guess < random_answer:
        return "<h1 style='color: red'>Too low, try again!</h1><p>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif guess > random_answer:
        return "<h1 style='color: blue'>Too high, try again!</h1><p>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return f"<h1 style='color: purple'>Bingo. The answer is {guess}.<p>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == '__main__':
    app.run(debug=True)
