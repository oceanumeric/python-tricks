"""
Python’s reduce() is a function that implements a mathematical technique called
folding or reduction. reduce() is useful when you need to apply a function to an
iterable and reduce it to a single cumulative value. Python’s reduce() is 
popular among developers with a functional programming background, but Python
has more to offer.
functional programming focus:
    the use of recursion
    process list or array
    focus on what is to be comuted

for instance, reduce works in this way:
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

Python’s reduce() can have remarkably bad performance because it works by 
calling functions multiple times. This can make your code slow and inefficient.
Using reduce() can also compromise the readability of your code when you use it
with complex user-defined functions or lambda functions.
"""


from functools import reduce
from operator import add


def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


numbers = [0, 1, 2, 3, 4]
reduce(my_add, numbers)
reduce(my_add, numbers, 100)
print(reduce(add, numbers))
print(reduce(lambda a, b: a * b, numbers))