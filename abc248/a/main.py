def main():
	import sys
	input = sys.stdin.readline

	s = input()
	ans = ""
	for i in range(0,10):
		a = str(i)
		if not a in s:
			print(a)
			break

if __name__ == '__main__':
  main()