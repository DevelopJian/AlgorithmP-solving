prime = [False, False] + [True] * (1_000_001 - 2)  # 인덱스 0~1000000
for i in range(2, 1_000_001):
    if prime[i] == True:
        for j in range(i * 2, 1_000_001, i):
            prime[j] = False

for tc in range(int(input())):
    n = int(input())

    cnt = 0
    for i in range(2, n//2+1) :  # 2 ~ n//2
        if (prime[i]== True) and (prime[n-i]== True):
            cnt += 1
    print(cnt)