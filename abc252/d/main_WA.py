def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()

import itertools

n = I()
a = LI()
seta = set()
for x in a:
	seta.add(x)
slist = list(seta)
x = list(itertools.combinations(slist,3))
print(len(x))