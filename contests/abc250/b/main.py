def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()

n,a,b = MI()

for i in range(n):
	for k in range(a):
		ans_row = ""
		for j in range(n):
			flg = "."
			if (i+j)%2==0:
				flg = "."
			else:
				flg = "#"
			for l in range(b):
				ans_row += flg
		print(ans_row)