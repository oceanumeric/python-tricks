"""
Functions
"""


def func_name(arg1, arg2):
    """Docstring starts wtih a short description.

    May have more information here.

    arg1 = something
    arg2 = somehting

    Returns something

    Example usage:

    func_name(1, 2)
    """
    result = arg1 + arg2

    return result

help(func_name)



def f(a, b, c, *args, **kwargs):
    return a, b, c, args, kwargs


print(f(1, 2, 3, 4, 5, 6, x=7, y=9, z=9))


# generators

def count(n=0):
    while True:
        yield n
        n += 1

for i in count(10):
    print(i)
    if i >= 15:
        break



def updown(n):
    yield from range(n)
    yield from range(n, 0, -1)

print(list(updown(5)))


# first class function
def double(x):
    return x*2

def twice(x, func):
    return func(func(x))

print(twice(3, double))


# function dispatch
def add(x, y):
    return x + y

def mul(x, y):
    return x * y

ops = {
    'a': add,
    'm': mul
}

items = zip('aammaammam', range(10), range(10))
for items in items:
    key, x, y = items
    op = ops[key]
    print(key, x, y, op(x, y))


# closure
def f(x):
    def g(y):
        return x + y
    return g

f1 = f(0)
f2 = f(10)
print(f1(5), f2(5))


# decorators
def timer(f):
    import time
    def g(*args, **kwargs):
        tic = time.time()
        res = f(*args, **kwargs)
        toc = time.time()
        return res, toc-tic
    return g



@timer
def g(n):
    s = 0
    for i in range(n):
        s += i
    return s

print(g(1000))


# map, filter and reduce
xs = range(10)
print(list(map(lambda x: x**2, xs)))
print(list(filter(lambda x: x%2 == 0, xs)))
from functools import reduce
print(reduce(lambda x, y: x+y, xs))

# iterools, functional and operator
import operator as op
import itertools as it
print(op.add(2, 3))
print(list(it.islice(it.cycle([1,2,3]), 1, 10)))
print(list(it.permutations('abc', 2)))

# function annotations
def f(a: str='Hello') -> bool:
    return a.islower()

print(f())
print(f('hello'))
print(f.__annotations__)

# Type and function annotations are NOT enforced. In fact, the Python interpreter essentially ignores them.

def f(x: int) -> int:
    return x + x

print(f("hello"))

