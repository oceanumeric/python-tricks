"""
f-strings in Python 3
"""

# old format
name = 'Eric'
print("hello, %s." % name)
age = 56
print("Hello, {}. You are {}.".format(name, age))

# f-string
name = "Eric"
age = 76
print(f"Hello, {name}. You are {age}")
print(f"{2 * 37}")
print(f"{name.lower()} is funny")


# implement it in a class
class Comedian:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"{self.firstname} {self.lastname} is {self.age}."

    def __repr__(self):
        return f"{self.firstname} {self.lastname} is {self.age}. Surprise!"


new_comedian = Comedian("Eric", "Idle", "74")
print(f"{new_comedian}")
print(f"{new_comedian !r}")


# multiline f-strings
name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)
print(message)

message = (
    f"Hi {name}. "
    f"You are a {profession}. " 
    f"You were in {affiliation}."
)
print(message)


# There are more you could learn, just read docs
# be cautions on " " and '' and inline comment and {}

age = 46
setup_code = f"I am {age} years old" if age > 30 else "haha"
print(setup_code)

age = 30
setup_code = f"I am {age} years old" if age > 30 else "this is string magic"
print(setup_code)

# you could even do this
fsort = "sorted"
array = [2, 6, 1, 90, 5]
# this is very useful when you want to pass it to stmt in timeit function
print(f"{fsort}({array})")  