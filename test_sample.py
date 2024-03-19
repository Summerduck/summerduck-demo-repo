# content of test_sample.py
def inc(x):
    return x + 1

def test_failed():
    assert inc(3) == 5

def test_passed():
    assert inc(4) == 5