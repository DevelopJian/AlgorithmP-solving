from collections import deque
import sys
input = sys.stdin.readline

n = int(input())  # 자료구조 개수
qs = list(map(int, input().split()))
val = list(map(int, input().split()))
queue = []

for i in range(n):
    if qs[i] == 0:
        queue.append(val[i])

m = int(input())
lst = list(map(int, input().split()))

queue.reverse()
result = deque(queue+lst)

for _ in range(m):
    print(result[0])
    result.popleft()