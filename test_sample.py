# content of test_sample.py
def increment(x):
    return x + 1

def test_failed():
    assert increment(3) == 5

def test_passed():
    assert increment(4) == 5