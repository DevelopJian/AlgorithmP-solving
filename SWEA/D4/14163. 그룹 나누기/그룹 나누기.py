def dfs(s):
    for node in lst[s]:
        if not v[node]:
            v[node] = 1
            dfs(node)

t = int(input())
for tc in range(1, t+1):

    n, m = map(int, input().split()) # 사람 수, 연결 수
    ipt = list(map(int, input().split()))
    lst = [[] for _  in range(n+1)] # 인접리스트 (양방향)

    for i in range(0, 2*m, 2):
        lst[ipt[i]].append(ipt[i+1])
        lst[ipt[i+1]].append(ipt[i])
    v = [0] * (n+1)
    ans = 0
    for i in range(1, n+1):
        if not v[i]:
            ans += 1  # dfs 함수 호출횟수
            v[i] = 1
            dfs(i)

    print(f'#{tc} {ans}')