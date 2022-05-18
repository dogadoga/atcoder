def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
import itertools

n,w = MI()
a = LI()

a += [0,0]
good = [False] * (w+1)

for k in range(n+2):
	for j in range(k):
		for i in range(j):
			weight = a[i] + a[j] + a[k]
			if weight <= w:
				good[weight] = True

print(good.count(True))