
# content of test_sample.py
def inc(x):
def inc(x,y):
    return x + 1


def foo(x):
    assert x

def test_foo(): foo()

def test_answer():
    assert inc(3) == 4


