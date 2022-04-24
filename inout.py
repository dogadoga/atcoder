# 整数

# 1 行 1 列
N = int(input())

# 1 行複数列
N, M = map(int, input().split())

# 1 行をリストに
a = list(map(int, input().split()))

# N 行 1 列をリストに
a = [int(input()) for i in range(N)]

# N 行複数列を 2 次元リストに
a = [list(map(int, input().split())) for i in range(N)]

# N 行 2 列
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

# N 行複数列を列ごとに異なるリストへ
abc = [map(int, input().split()) for _ in range(N)]
a, b, c = [list(i) for i in zip(*abc)]

# 文字列を数字にしてリストに追加 ('1122'とかを[1,1,2,2]に)
n = [int(x) for x in input()]


# 文字列---------------------------------------------

# 1行に1つ
s = input()

# 1行に複数
s, t = input().split()

# 1行スペースなし (リストに)
s = list(input)

# 1行スペースあり (リストに)
s = input().split()

# 複数行1列をリストに
a = [input() for i in range(n)]

# 複数行 (2次元リストに)
g = [list(input()) for i in range(n)]

#sysを使った定義
# import sys
# def I(): return int(sys.stdin.readline().rstrip())
# def MI(): return map(int,sys.stdin.readline().rstrip().split())
# def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
# def S(): return sys.stdin.readline().rstrip()
# def LS(): return list(sys.stdin.readline().rstrip())

# 普通の定義
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def LS(): return list(input())

# リストを出力
# アスタリスクをつけてアンパックできる
# s = [1, 2, 3, 4, 5]
print(*s)  # 1 2 3 4 5
print(*s, sep='-')  # 1-2-3-4-5