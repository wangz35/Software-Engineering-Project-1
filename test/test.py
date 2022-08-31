try:
    import vowelcheck as v
except ImportError as e:
    import sys
    sys.path.append("../")

#import vowelcheck as v
def test_uppercase_vowel():
    assert(v.vowel("A")) == 1
def test_lowercase_vowel():
    assert(v.vowel("e")) == 1
def test_uppercase_consonant():
    assert(v.vowel("B")) == 0
def test_lowercase_consonant():
    assert(v.vowel("n")) == 0
    
test_uppercase_vowel()
test_lowercase_vowel()
test_uppercase_consonant()
test_lowercase_consonant()
