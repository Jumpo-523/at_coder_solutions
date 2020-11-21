# https://atcoder.jp/contests/arc108/tasks/arc108_a

# 二次方程式を解く解が整数かどうかを見る。

# これは下記の理由でボツ解答
# S=1000000000000 
# P=1
# とすると、S**2 - 4*P == 999999999999999999999996
# となる。これをmath.sqrtに渡しても正しい計算をしてくれない!

# 最初のPに関して平方根をとり、n =1:√Pで全探索すればいいらしい。。

import math
def solve_eq(S, P):
    import pdb; pdb.set_trace()
    root_part = S**2 - 4*P
    print(root_part)
    if root_part >= 0:
        x = S - root_part
        if x % 2 == 0:
            print(x)
            print("Yes")
        else:
            print("No")
    else:
        print("No")

# foxを再帰的に取り除くが、１個なぜかRE...
# 答えが知りたい。
# 1個だけ
def extract_fox(s):
    import re
    if s.count("fox"):
        s = re.sub(string=s, repl="", pattern="fox")
        s = extract_fox(s)
    return s

if __name__ == "__main__":
    answer = "b"
    if answer == "a":
        # https://atcoder.jp/contests/arc108/tasks/arc108_a
        S, P = list(map(int, input().split()))
        solve_eq(S, P)
    elif answer == "b":
        s = input()
        print(len(extract_fox(s)))


