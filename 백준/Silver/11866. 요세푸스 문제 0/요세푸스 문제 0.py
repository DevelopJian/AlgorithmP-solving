# 실제로 리스트를 돌리는게 아니라 보는 위치만 돌리는 방법
# 메모리, 시간 훨씬 아낌.

n, m = map(int, input().split())

lst = list(range(1, n + 1))
result = []

now = 0
for _ in range(n):
    now += m - 1
    if now >= len(lst):
        now %= len(lst)
    result.append(str(lst.pop(now)))

print('<', ', '.join(result), '>', sep='')