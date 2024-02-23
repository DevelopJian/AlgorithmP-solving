n, m = map(int, input().split())
card = list(map(int, input().split()))
mx = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sm = card[i] + card[j] + card[k]
            if mx < sm <= m:
                mx = sm
print(mx)