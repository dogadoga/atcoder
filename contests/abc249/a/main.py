def main():
	import sys
	input = sys.stdin.readline

	a,b,c,d,e,f,x = map(int, input().split())

	T: int = 0
	A: int = 0

	T = (a*(x//(a+c))+min(x%(a+c),a))*b
	A = (d*(x//(d+f))+min(x%(d+f),a))*e

	if T>A:
		print("Takahashi")
	elif A>T:
		print("Aoki")
	else:
		print("Draw")

if __name__ == '__main__':
  main()