import time


def delay_decorator(function):
    def wrapper_function():
        function()
        function()
        function()

    return wrapper_function


@delay_decorator
def say_hello():
    print("hello")


def say_greeting():
    print("greetings")


say_hello()
say_greeting()
