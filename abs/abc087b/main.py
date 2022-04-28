import sys
input = sys.stdin.readline
def I(): return int(input().rstrip())
def MI(): return map(int, input().rstrip().split())
def LI(): return list(map(int,input().rstrip().split()))
def S(): return input().rstrip()
def LS(): return list(input().rstrip())

def main():
	a = I()
	b = I()
	c = I()
	x = I()
	count = 0

	for i in range(a+1):
		for j in range(b+1):
			for k in range(c+1):
				if i*500 + j*100 + k*50 == x:
					count += 1

	print(count)

if __name__ == "__main__":
	main()