from um import count

def test_count_no_um():
    assert count("Hello") == 0
    assert count("How are you?") == 0

def test_count_multiple_um():
    assert count("um, hello, um, world") == 2

def test_count_um_in_word():
    assert count("yummy") == 0