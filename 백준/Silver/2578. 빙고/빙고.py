import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(5)]
# 사회자가 부르는 숫자 1차원 배열 생성
lst = []
for i in range(5):
    lst += list(map(int, input().split()))
# 번호마다 좌표위치 저장 (인덱스 = 빙고판에 있는 수, 값 = 좌표)
# -> 사회자가 수를 부르면 좌표를 바로 알 수 있도록
pos_lst = [0]*26
for i in range(5):
    for j in range(5):
        pos_lst[arr[i][j]] = (i, j)

v = [[0]*10 for _ in range(4)] #v0~v3 빈도수 체크 # TODO 왜 *10? 넉넉잡아?
for n in lst:
    i, j = pos_lst[n]
    v[0][i] += 1  # 가로갯수 누적
    v[1][j] += 1  # 세로갯수 누적
    v[2][i+j] += 1  # / 갯수 누적
    v[3][i-j] += 1  # \ 갯수 누적
    cnt = 0
    for tlst in v:
        cnt += tlst.count(5)
    if cnt >= 3:
        break
print(sum(v[0]))  # 표시 누적된 횟수 = 사회자가 부른 횟수