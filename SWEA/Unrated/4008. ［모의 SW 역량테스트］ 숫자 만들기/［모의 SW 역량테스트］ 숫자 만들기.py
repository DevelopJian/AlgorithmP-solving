def dfs(num, total): # 이번에 연산할 숫자 인덱스, 지금까지 계산한 수
    global mx, mn
    # 종료조건, 정답처리
    if num == n:
        mx = max(total, mx)
        mn = min(total, mn)
        return
    # 재귀호출
    if opr[0]:
        opr[0] -= 1
        dfs(num + 1, total + nums[num])
        opr[0] += 1 # 원상복구
    if opr[1]:
        opr[1] -= 1
        dfs(num + 1, total - nums[num])
        opr[1]  += 1
    if opr[2]:
        opr[2] -= 1
        dfs(num + 1, total * nums[num])
        opr[2] += 1
    if opr[3] and nums[num]:
        opr[3] -= 1
        # 음수 나누기 주의
        dfs(num + 1, int(total / nums[num]))
        opr[3] += 1

t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 숫자갯수
    opr = list(map(int, input().split())) # n-1개 : + - * //
    nums = list(map(int, input().split()))

    mx, mn = float('-inf'), float('inf')
    dfs(1, nums[0])

    print(f'#{tc} {mx-mn}')