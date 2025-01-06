from bank import value

def test_start_hello()
    assert value("hello") == 0
    assert value("Hello Lavanya") == 0

def test_start_h():
    assert value("How are you?") == 20
    assert value("How you doing?") == 20

def test_not_start_h():
    assert value("What's happening") == 100
    
