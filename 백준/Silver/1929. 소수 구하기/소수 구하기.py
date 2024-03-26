import sys
input = sys.stdin.readline

m, n = map(int, input().split())
sosu = [False, False] + [True]*(n-1)   # n+1개(인덱스 0~n)

for i in range(2, n+1) :
    if sosu[i] == True :
        for j in range(i*2, n+1, i):
            sosu[j]= False

for i in range(m, n+1):  # m~n
    if sosu[i] == True :
        print(i)