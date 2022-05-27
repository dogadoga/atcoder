def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
INF = 1000000
n = I()
s = [input() for i in range(n)]
ans = INF

for i in range(10):
	tmp = s.copy()
	time = 0
	flg = True
	while flg:
		for reel in tmp:
			sec = time%10
			if int(reel[sec]) == i:
				tmp.remove(reel)
				break
		if len(tmp) == 0:
			break
		time += 1
	ans = min(ans,time)

print(ans)


