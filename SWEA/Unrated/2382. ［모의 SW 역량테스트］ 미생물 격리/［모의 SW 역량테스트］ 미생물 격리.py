t = int(input())
for tc in range(1, t + 1):
    n, m, k = map(int, input().split())  # 셀 갯수, 격리시간, 군집개수
    lst = [list(map(int, input().split())) for _ in range(k)]  # 군집정보
    dir = {1: 2, 2: 1, 3: 4, 4: 3}  # 방향 반대로 바꾸기 딕셔너리
    time = 0
    while time < m:
        time += 1
        i = 0
        while i < len(lst):
            # 이동시키기 (최초는 약품 위에 있지않음)
            if lst[i][3] == 1:  # dir
                lst[i][0] -= 1
            elif lst[i][3] == 2:
                lst[i][0] += 1
            elif lst[i][3] == 3:
                lst[i][1] -= 1
            elif lst[i][3] == 4:
                lst[i][1] += 1
            # 이동 후 약물 위라면
            if lst[i][0] == 0 or lst[i][0] == n - 1 or lst[i][1] == 0 or lst[i][1] == n - 1:
                lst[i][2] //= 2  # 1. 군집수//2
                if lst[i][2] == 0:
                    lst.pop(i)
                    i -= 1
                else:
                    lst[i][3] = dir[lst[i][3]]  # 2. 미생물 남았다면 방향 반대로 바꾸기
            i += 1  # 리스트 안없어진 경우에만 i += 1 됨

        # 군집 합하고 없애기
        lst.sort(reverse=True)  # 세로->가로-> 미생물수(큰 순서)
        idx = 1
        while idx < len(lst):
            # 앞에것과 같은 위치에 있다면
            if lst[idx][0] == lst[idx - 1][0] and lst[idx][1] == lst[idx - 1][1]:
                lst[idx - 1][2] += lst[idx][2]  # 군집수 합하기
                lst.pop(idx)
            # 아니라면 -> 밑에것 탐색하기
            else:
                idx += 1

    # 남아있는 미생물수 구하기
    ans = 0
    for l in lst:
        ans += l[2]

    print(f'#{tc} {ans}')