# ����

# 1 �s 1 ��
N = int(input())

# 1 �s������
N, M = map(int, input().split())

# 1 �s�����X�g��
a = list(map(int, input().split()))

# N �s 1 ������X�g��
a = [int(input()) for i in range(N)]

# N �s������� 2 �������X�g��
a = [list(map(int, input().split())) for i in range(N)]

# N �s 2 ��
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

# N �s�������񂲂ƂɈقȂ郊�X�g��
abc = [map(int, input().split()) for _ in range(N)]
a, b, c = [list(i) for i in zip(*abc)]

# ������𐔎��ɂ��ă��X�g�ɒǉ� ('1122'�Ƃ���[1,1,2,2]��)
n = [int(x) for x in input()]


# ������---------------------------------------------

# 1�s��1��
s = input()

# 1�s�ɕ���
s, t = input().split()

# 1�s�X�y�[�X�Ȃ� (���X�g��)
s = list(input)

# 1�s�X�y�[�X���� (���X�g��)
s = input().split()

# �����s1������X�g��
a = [input() for i in range(n)]

# �����s (2�������X�g��)
g = [list(input()) for i in range(n)]

#sys���g������`
# import sys
# def I(): return int(sys.stdin.readline().rstrip())
# def MI(): return map(int,sys.stdin.readline().rstrip().split())
# def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
# def S(): return sys.stdin.readline().rstrip()
# def LS(): return list(sys.stdin.readline().rstrip())

# ���ʂ̒�`
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def LS(): return list(input())

# ���X�g���o��
# �A�X�^���X�N�����ăA���p�b�N�ł���
# s = [1, 2, 3, 4, 5]
print(*s)  # 1 2 3 4 5
print(*s, sep='-')  # 1-2-3-4-5