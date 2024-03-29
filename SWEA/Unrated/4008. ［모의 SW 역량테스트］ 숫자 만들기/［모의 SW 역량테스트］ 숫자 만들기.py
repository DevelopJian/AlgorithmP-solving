def dfs(num, total, add, sub, mul, div): # 이번에 연산할 숫자 인덱스, 지금까지 계산한 수
    global mx, mn
    # 종료조건, 정답처리
    if num == n:
        if mx < total:
            mx = total
        if mn > total:
            mn = total
        return
    # 재귀호출
    if add:
        dfs(num + 1, total + nums[num], add-1, sub, mul, div )
    if sub:
        dfs(num + 1, total - nums[num], add, sub-1, mul, div)
    if mul:
        dfs(num + 1, total * nums[num], add, sub, mul-1, div)
    if div and nums[num]:
        # 음수 나누기 주의
        dfs(num + 1, int(total / nums[num]), add, sub, mul, div-1)

t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 숫자갯수
    opr = list(map(int, input().split())) # n-1개 : + - * //
    nums = list(map(int, input().split()))

    mx, mn = float('-inf'), float('inf')
    dfs(1, nums[0], opr[0], opr[1], opr[2], opr[3])

    print(f'#{tc} {mx-mn}')