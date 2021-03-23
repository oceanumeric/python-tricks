from .package1 import foo  # relative import

def test_fun1():
    assert foo.fun1(4, 5) == 9