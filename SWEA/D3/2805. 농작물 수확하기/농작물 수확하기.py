t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 홀수
    ctr = n//2 # 중간점 인덱스
    products = [list(map(int, input())) for _ in range(n)]

    start = ctr+1  # 더하기 시작 인덱스
    nums = -1 # 더할 값 갯수
    total = 0

    for i in range(n):
        if i <= ctr:
            start -= 1
            nums += 2
            for num in range(nums): # 갯수만큼 반복
                total += products[i][start+num]
        else: # i>ctr
            start += 1
            nums -= 2
            for num in range(nums):
                total += products[i][start+num]

    print(f'#{tc} {total}')