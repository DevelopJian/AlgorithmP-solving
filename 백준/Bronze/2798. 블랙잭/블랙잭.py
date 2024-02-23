n, m = map(int, input().split())
card_list = list(map(int, input().split()))

sums = 0
mx = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sums = card_list[i] + card_list[j] + card_list[k]
            if mx <= sums <= m:
                mx = sums

print(mx)