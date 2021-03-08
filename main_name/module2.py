"""
Understand __name__ == "__main__"
"""
from module1 import *
import module3 as md

print("hello world")  # you are support to see another print

y = md.import_run(5, 6)
print(y)


