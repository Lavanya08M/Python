from plates import is_valid

def test_start_two_letters():
    assert is_valid("Aq12") == True
    assert is_valid("ab") == True
    assert is_valid("a123") == False
    
def test_not_start_with_letters():
        assert is_valid("12D") == False
        assert is_valid("12") == False

def test_length():
    assert is_valid("a") == False
    assert is_valid("AbcdefG") == False
    assert is_valid("ABS4") == True

def test_middle_numbers():
    assert is_valid("AB3DF") == False
    assert is_valid("AV49") == True

def test_first_number():
    assert is_valid("ABS04") == False
    assert is_valid("ED50") == True

def test_space_period_punctuation():
    assert is_valid("AB.CD") == False
    assert is_valid("AB CD") == False
    assert is_valid("AB!CD") == False
