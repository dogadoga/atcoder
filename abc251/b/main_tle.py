def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()

n,w = MI()
a = LI()

count = 0
for i in range(1,w+1):
	flg = False
	for j in range(n):
		if flg: break
		if a[j] == i:
			count += 1
			#print(1,"w:",i,"j:",j,"ans:",count)
			break
		for k in range(j+1,n):
			if flg: break
			if a[j]+a[k] == i:
				count += 1
				flg = True
				# print(2,"w:",i,"j:",j,"k:",k,"ans:",count)
				break
			for l in range(k+1,n):
				if a[j]+a[k]+a[l] == i:
					count += 1
					flg = True
					#print(3,"w:",i,"j:",j,"k:",k,"l:",l,"ans:",count)
					break
print(count)