from programs.listofsquares import list_of_squares

def test_list_of_squares():
    assert list_of_squares(2) == {1:1, 2:4}
    assert list_of_squares(3) == {1:1, 2:4, 3:9}
    assert list_of_squares(4) == {1:1, 2:4, 3:9, 4:16}