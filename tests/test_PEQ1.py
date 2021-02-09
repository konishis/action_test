import peq1


def test_peq1():
    result = peq1.aaa(3, 5, 10)
    assert result == 23
    
def test_ans():
    result = peq1.aaa(3, 5, 1000)
    assert result == 233168
