def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()

from collections import Counter

def comb(n,r):
	num = 1
	den = 1
	for i in range(r):
		num*=(n-i)
		den*=(r-i)
	return num//den

n = I()
a = LI()
c = Counter(a)
ans = comb(n,3)
for x in c.values():
	ans -= comb(x,2)*(n-x) #2つが被るとき
	ans -= comb(x,3) #3つが被るとき
print(ans)