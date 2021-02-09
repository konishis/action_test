'''
3 または 5 の倍数である 10 未満のすべての自然な数値をリストすると、3、5、6、9 が得られます。これらの倍数の合計は 23 です。

1000 以下の 3 または 5 のすべての倍数の合計を検索します。
'''

def calnumset(numrange, versusnum):
    numset = {num for num in range(1,numrange) if num % versusnum == 0}
    return numset


def aaa(num1, num2, range):
    return sum(calnumset(range, num1) | calnumset(range, num2))
