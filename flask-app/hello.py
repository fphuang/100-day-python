from flask import Flask
import random
import time

# __name__: __
app = Flask(__name__)

print(__name__)
print(random.__name__)

# export FLASK_APP="hello.py"
# flask run


# python decorator
@app.get('/')
def hello_word():
    return "<h1 style='text-align: center'>Hello, world!</h1>" \
           "<img src='https://icatcare.org/app/uploads/2019/09/The-Kitten-Checklist-1.png'> " \
           "<br> <img src='https://c.tenor.com/7fea_o7VelYAAAAC/cartoon-kitten.gif'>"


def make_bold(func):
    def bold():
        return f"<b>{func()}</b>"
    return bold


def make_emphasis(func):
    def emphasis():
        return f"<em>{func()}</em>"
    return emphasis


def make_underlined(func):
    def underlined():
        return f"<u>{func()}</u>"
    return underlined


@app.get('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Bye-bye!'


@app.route('/username/<name>/<int:number>')
def greet(number, name):
    return f"hello {name}, you are {number} years old."


if __name__ == '__main__':
    app.run(debug=True)
