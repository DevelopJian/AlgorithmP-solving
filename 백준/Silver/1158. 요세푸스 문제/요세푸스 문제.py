from collections import deque

n, k = map(int, input().split())
circle = deque(range(1, n+1))
result = []
while circle:
    circle.rotate(-k+1)
    r = circle.popleft()
    result.append(r)

print('<', end = '')
print(*result, sep = ', ', end = '')
print('>')
