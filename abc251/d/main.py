def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()

w = I()
ans = []
for i in range(1,101): 
	ans.extend((i, 100*i, 10000*i))
print(len(ans))
print(*ans)