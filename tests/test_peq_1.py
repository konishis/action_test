import peq_1


def test_peq_1():
    result = peq_1.aaa(3, 5, 10)
    assert result == 23
    
def test_ans():
    result = peq_1.aaa(3, 5, 1000)
    assert result == 233168
