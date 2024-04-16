n, k = map(int, input().split())

def bino_coef(n, k):
    if k == 0 or k == n:
        return 1
    return bino_coef(n-1, k) + bino_coef(n-1, k-1)

ans = bino_coef(n, k)
print(ans)