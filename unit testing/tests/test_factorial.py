from programs.factorial import fact

def test_fact():
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(10) == 3628800