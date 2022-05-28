# 組合せを数える
def comb(n,r):
	num = 1
	den = 1
	for i in range(r):
		num*=(n-i)
		den*=(r-i)
	return num//den