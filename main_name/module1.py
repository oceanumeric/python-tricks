"""
Understand __name__ == "__main__"

There are two primary ways that you can instruct the Python interpreter to execute or use code:

You can execute the Python file as a script using the command line.
You can import the code from one Python file into another file or into the interactive interpreter.
"""

print("You are importing module 1 right now")


if __name__ == "__main__":
    print("I don't think you would see me when you import me to thers")

