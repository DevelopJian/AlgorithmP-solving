def factorial(k):
    result = 1
    for i in range(2, k+1):
        result *= i
    return result

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    ans = factorial(m) // (factorial(n) * factorial(m-n))
    print(ans)