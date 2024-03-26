T = int(input())
for tc in range(T):
    ia, ib = map(int, input().split())
    a, b = max(ia,ib), min(ia, ib) # a가 큰수임

    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            gongyak = i
            break

    result = a * b // gongyak
    print(result)

