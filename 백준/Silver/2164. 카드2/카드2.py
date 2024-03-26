from collections import deque

n = int(input())
cards = deque(range(1, n+1))

for _ in range(n-1):
    cards.popleft()
    cards.rotate(-1)

print(*list(cards))