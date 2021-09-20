"""
Handling missing keys in dictionaries
"""
from collections import defaultdict


a_dict = {}
a_dict.setdefault('missing_key', 'default value')
print(a_dict['missing_key'])
# print(a_dict['nokey'])

print(issubclass(defaultdict, dict))  # is a subclass

def_dict = defaultdict(list)  # pass list to .default_factor
def_dict['one'] = 1
def_dict['missing']
def_dict['another_missing'].append(4)
print(def_dict)

# Here, you pass list to .default_factory when you create the dictionary.
# Then, you use def_dict just like a regular dictionary. Note that when you
# try to access or modify the value mapped to a non-existent key, the
# dictionary assigns it the default value that results from calling list().

# python defaultdict type solves the following common programming:
# - grouping
# - counting
# - accumulating

dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]

dep_dd = defaultdict(list)
for department, employee in dep:
    dep_dd[department].append(employee)

print(dep_dd)

# if you have duplicated values, initialize defaultdict with set
dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe')]

dep_dd = defaultdict(set)
for department, employee in dep:
    dep_dd[department].add(employee)

print(dep_dd)

# There are more to explroe, visit: https://realpython.com/python-defaultdict/
