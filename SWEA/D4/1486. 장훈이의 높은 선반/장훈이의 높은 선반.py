from itertools import combinations

t = int(input())
for tc in range(1, t+1):
    n, b = map(int, input().split())
    h = list(map(int, input().split()))
    mn = 10000 * n
    for i in range(1, n+1): # i = 쌓은 점원수
        for j in combinations(h, i):
            if b<= sum(j) < mn:
                mn = sum(j)

    print(f'#{tc} {mn-b}')