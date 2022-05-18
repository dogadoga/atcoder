def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()

s = S()
x = len(s)

y = 6//x

ans = ""
for i in range(y):
	ans += s

print(ans)