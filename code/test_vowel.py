import vowel as c
def test_uppercase_vowel():
    assert(c.vowel("A")) == 1
def test_lowercase_vowel():
    assert(c.vowel("e")) == 1
def test_uppercase_consonant():
    assert(c.vowel("b")) == 0
def test_capital_consonant():
    assert(c.vowel("n")) == 0
