
# content of test_sample.py
def inc(x):
    return x + 1


def foo():
    assert False

def test_foo(): foo()

def test_answer():
    assert inc(3) == 5


