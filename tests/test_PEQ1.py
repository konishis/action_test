"""
3 または 5 の倍数である 10 未満のすべての自然な数値をリストすると、3、5、6、9 が得られます。これらの倍数の合計は 23 です。

1000 以下の 3 または 5 のすべての倍数の合計を検索します。
"""
from PEQ1 import PEQ1

def test_PEQ1_default(capsys):
    PEQ1.aaa(3, 5, 10)
    out, err = capsys.readouterr()
    assert out == 55
    
