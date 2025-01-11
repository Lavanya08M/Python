from numb3rs import validate

def test_invalid_address():
    assert validate("1.2.3.1000") == False
    assert validate("512.512.512.512") == False
    assert validate("cat") == False
    assert validate("1.2.3") == False

def test_valid_address():
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True