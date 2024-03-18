# 이진트리로 하기
def dfs(idx, sm): # 직원 인덱스, 키의 합
    global mn
    # 가지치기(이미 정답가능성 없음)
    if sm >= mn:
        return
    # 종료조건
    if idx == n:
        # 정답처리
        if b <= sm < mn:
            mn = sm
        return
    # dfs 호출
    dfs(idx + 1, sm + h[idx])
    dfs(idx + 1, sm)

t = int(input())
for tc in range(1, t+1):
    n, b = map(int, input().split())
    h = list(map(int, input().split()))
    # 키의 합이 b이상인 것 중 제일 작은 것 구하기
    mn = 10000 * n  # 키의 합 중 최소
    dfs(0, 0)

    print(f'#{tc} {mn-b}')