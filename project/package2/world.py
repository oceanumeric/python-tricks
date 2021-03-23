import sys
sys.path.append('.')

from hello import fun2
from package1.foo import fun1

print(fun2(2, 5))
print(fun1(2, 5))