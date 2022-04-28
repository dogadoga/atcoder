import sys
input = sys.stdin.readline
def I(): return int(input().rstrip())
def MI(): return map(int, input().rstrip().split())
def LI(): return list(map(int,input().rstrip().split()))
def S(): return input().rstrip()
def LS(): return list(input().rstrip())

def insertion_sort(data):
    for i in range(1, len(data)):
        tmp = data[i]         #挿入データを一時的に記録
        j = i - 1
        while (j >= 0) and (data[j] > tmp):   #挿入データがソート済みデータ内のデータよりも小さく右にある
            data[j + 1] = data[j]       #右へ1つデータを移す
            j -= 1
        data[j + 1] = tmp     #上の操作で移動を終えた所に一時的に記録していた挿入データを代入
    return data

def main():
	n = I()
	a = LI()
	alice = 0
	bob = 0

	sorted_a = insertion_sort(a)
	for i,n in enumerate(sorted_a):
		if i%2==0:
			alice += n
		else:
			bob += n
	ans = alice - bob
	print(ans)

if __name__ == "__main__":
	main()