def dfs(cnt): # cnt = 교환한 횟수
    global mx  # 참조만 하는게 아니라 할당까지 해줘야하니까 글로벌
    # 가지치기(같은 레벨에 있는 같은 숫자리스트가 있으면 한개빼고 종료)
    if (cnt, int(''.join(nums))) in history:
        return
    history.add((cnt, int(''.join(nums)))) # histroy 에 없다면 (레벨, 숫자) 기록
    # 종료조건
    if cnt == m:
        mx = max(mx, int(''.join(nums)))
        return
    # 바꿀 좌표 골라주기
    for i in range(l-1):
        for j in range(i+1, l):
            nums[i], nums[j] = nums[j], nums[i]
            dfs(cnt +1)
            nums[i], nums[j] = nums[j], nums[i] # 초기화!!!

t = int(input())
for tc in range(1, t+1):
    nums, m = input().split()
    m = int(m)
    nums = list(nums)
    l = len(nums)
    mx = 0
    history = set()  # 중복 제거 위한 기록 만들기
    dfs(0)

    print(f'#{tc} {mx}')