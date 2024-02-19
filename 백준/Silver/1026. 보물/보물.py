n = int(input())

a = list(map(int, input().split()))
a.sort()
b = list(map(int, input().split()))
b = reversed(sorted(b))

print(sum( i * j for i, j in zip(a, b)))