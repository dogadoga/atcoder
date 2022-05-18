def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()

n = I()
ans = 0
poems = []
highest = -1
for i in range(n):
	s,t = input().split()
	t = int(t)
	if s not in poems:
		poems.append(s)
		if t > highest:
			ans = i+1
			highest = t

print(ans)