def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()

n,k = MI()
a = LI()
b = LI()

def my_index_multi(l, x):
    return [i for i, _x in enumerate(l) if _x == x]

tmp = max(a)
tmp_l = my_index_multi(a,tmp)

flg = False
for x in tmp_l:
	if x+1 in b:
		flg = True

if flg: print("Yes")
else: print("No")