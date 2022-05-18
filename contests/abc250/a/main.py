def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()

h,w = MI()
r,c = MI()

ans = 0
if h==1 and c==1:
	ans = 0
elif h == 1:
	if c == 1 or c == w:
		ans = 1
	else:
		ans = 2
elif w == 1:
	if r == 1 or r == h:
		ans = 1
	else:
		ans = 2
else:
	if r == 1 or r == h:
		if c == 1 or c == w:
			ans = 2
		else:
			ans = 3
	elif c == 1 or c == w:
		ans = 3
	else:
		ans = 4

print(ans)