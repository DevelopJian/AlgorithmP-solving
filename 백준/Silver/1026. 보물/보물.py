### 내방법 ###
# 로직
# heapq 사용 -> A최댓값정렬 B최솟값정렬
# 같은 인덱스끼리 곱해서 합구하기
from heapq import heappop, heappush, heapify
# 작은것 * 큰것으로 해야 최소 -> B의 크기순서 역순으로 A를 정렬
n = int(input())
A = list(map(int, input().split()))
# A 최솟값정렬 (이진트리형식 -> 인덱스사용말고 하나씩 pop해서 써야함)
heapify(A)
# B 최댓값정렬
B = []
for num in map(int, input().split()) :
    heappush(B, (-num, num))

total = 0
for idx in range(n):
    summ = heappop(A) * heappop(B)[1]
    total += summ
print(total)

### 다른방법 ###
n = int(input())

a = list(map(int, input().split()))
a.sort()
b = list(map(int, input().split()))
b = reversed(sorted(b))

print(sum( i * j for i, j in zip(a, b)))
