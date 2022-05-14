import sys
input = sys.stdin.readline
def I(): return int(input().rstrip())
def MI(): return map(int, input().rstrip().split())
def LI(): return list(map(int,input().rstrip().split()))
def S(): return input().rstrip()
def LS(): return list(input().rstrip())

def main():
  N = I()
  A = LI()
  flag = True
  count = 0

  while flag:
      for i, a in enumerate(A):
          if a % 2 != 0:
              flag = False
              break
          else:
              A[i] = a / 2
      if flag:
          count += 1
  print(count)
  
if __name__ == '__main__':
  main()