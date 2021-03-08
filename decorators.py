"""
decorators
"""
import functools

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


print(say_whee())


def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)
    return inner_function()


outer_function()


def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)
    return inner_function


my_func = outer_function()
my_func()


def outer_function(msg):
    def inner_function():
        print(msg)  # closure
    return inner_function


hi_function = outer_function('Hi')
bye_function = outer_function('Bye')
hi_function()
bye_function()


def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function


def display():
    print("display function ran")


decorated_function = decorator_function(display)
decorated_function()


# why we need decorators
def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed this before{}".format(original_function.__name__))
        return original_function()
    return wrapper_function


def display():
    print("display function ran")


decorated_function = decorator_function(display)
decorated_function()


def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed this before{}".format(original_function.__name__))
        return original_function()
    return wrapper_function


@decorator_function
def display():
    print("display function ran")


display()