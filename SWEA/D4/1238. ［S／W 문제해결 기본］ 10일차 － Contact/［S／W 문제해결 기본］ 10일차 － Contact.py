# visit 배열 중 최대숫자의 인덱스 중 젤큰것 구하기
# 최대숫자가 여러명일 수도 있는 경우 고려
from collections import deque
def bfs(s):
    q = deque([s])
    v = [0] * 101
    v[s] = 1
    mxidx = 0
    mx = 0
    while q:
        n = q.popleft()
        for i in adj[n]:
            if not v[i]:
                q.append(i)
                v[i] = v[n] + 1
                if v[i] == mx:
                    if i > mxidx:
                        mxidx = i
                elif v[i] > mx:
                    mx, mxidx = v[i], i
    return mxidx

for tc in range(1,11):
    l, start = map(int, input().split())
    lst = list(map(int, input().split()))
    adj = [[] for _ in range(101)] # 연락 가능한 리스트 // 0은 안씀
    for i in range(0,l,2):
        adj[lst[i]].append(lst[i+1])  #단방향

    print(f'#{tc} {bfs(start)}')