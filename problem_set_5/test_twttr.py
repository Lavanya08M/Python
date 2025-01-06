from twttr import shorten

def test_consonants():
    assert shorten("CSCHCK") == "CSCHCK"

def test_numbers():
    assert shorten("50123") == "50123"

def test_capitalized_vowels():
    assert shorten("Apple") == "ppl"

def test_lowercase_vowels():
    assert shorten("Twitter") == "Twttr"

def test_word_punctuation():
    assert shorten("David, Malon") == "Dvd, Mln"

