import sys
input = sys.stdin.readline
def I(): return int(input().rstrip())
def MI(): return map(int, input().rstrip().split())
def LI(): return list(map(int,input().rstrip().split()))
def S(): return input().rstrip()
def LS(): return list(input().rstrip())

a = I()
b,c = MI()
s = S()
print(f"{a+b+c} {s}")
