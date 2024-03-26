from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())

deq = deque()  # 진짜 쓸것!!
de = deque(map(int, input().split())) # 임시로 받은것
for i in range(1, n+1):
    deq.append((i, de[0])) # (인덱스, 값)
    de.popleft()

result = [] # 터진 순서

for _ in range(n):
    idx, val = deq.popleft()
    result.append(idx)
    if val > 0:
        deq.rotate(-(val-1))
    else :
        deq.rotate(-val)

print(*result)