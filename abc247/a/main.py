def main():
	import sys
	input = sys.stdin.readline

	from collections import deque

	q = deque(map(int, input().rstrip()))
	q.pop()
	q.appendleft(0)
	print("".join(q))
if __name__ == '__main__':
  main()