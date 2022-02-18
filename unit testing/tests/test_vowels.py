from programs.vowels import vowels

def test_vowels():
    assert vowels('Hello') == 2
    assert vowels('Hello World') == 3
    assert vowels('Lorem ipsum dolor sic amet') == 9