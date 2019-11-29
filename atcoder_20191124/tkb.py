

# A
"""今日の曜日を表す文字列 S が与えられます。
次の日曜日 (あす以降) が何日後か求めてください。"""
dayofweek = input()
days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
output = days.index("SUN") - days.index(dayofweek) if dayofweek != "SUN" else 7
print(output)

# B
"""英大文字のみからなる文字列 S があります。また、整数 N が与えられます。
S の各文字を、アルファベット順で N 個後の文字に置き換えた文字列を出力してください。ただしアルファベット順で Z の 1 個後の文字は A とみなします。"""



N = int(input())
S = input()
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def get_str_leading_n(string, alphabets, N):
    index_ = (alphabets.index(string.upper()) + N) % 26
    return alphabets[index_]
output = "".join(list(map(lambda p: get_str_leading_n(p, alphabets, N), S)))
print(output)


"""高橋くんは整数を 1 つ買いに整数屋さんに行きました。
整数屋さんには 1 以上 10**9 以下の整数が売られていて、整数 N を買うためには 
A×N + B×d(N) 円が必要です。ここで、d(N) は N の十進表記での桁数です。

高橋くんの所持金が 
X 円のとき、高橋くんの買うことのできる最も大きい整数を求めてください。
ただし、買うことのできる整数が 1 つもない場合は 
0 を出力してください。"""


# E

"""全ての要素のあまりを求めておく"""


N, K = list(map(int, input().split()))
An = list(map(int, input().split()))
An = [elem%K for elem in An]
count = 0
for i in range(len(An)):
    for k in range(1,K):
        if i - j == sum(An[i:i+k])%K:
            count += 1
print(count)


# F - Sugoroku

N, M = list(map(int, input().split()))
S = input()
"""
9 3
0001000100
"""
# 動的計画法を用いてバックワードにといていく
