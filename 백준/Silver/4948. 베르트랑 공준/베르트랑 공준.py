import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    else :
        sosu = [False, False] + [True] * (2*n-1) # 인덱스 0~ 2n

        for i in range(2, 2*n+1):
            if sosu[i] == True :
                for j in range(i*2, 2*n+1, i):
                    sosu[j] = False
        cnt = 0
        for i in range(n+1, 2*n+1): # n+1 ~ 2n
            if sosu[i] == True :
                cnt += 1
        print(cnt)
