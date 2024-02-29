king, rock, n = input().split()
k = [int(king[1]), king[0]] # 행열 좌표
r = [int(rock[1]), rock[0]]
n = int(n)
# 열좌표를 숫자로 바꿔줌
col = '0ABCDEFGH'
for idx, alh in enumerate(col):
    if alh == k[1]:
        k[1] = int(idx)
    if alh == r[1]:
        r[1] = int(idx)

board = [[0]*9 for _ in range(9)]  # 0번째 행열 안쓰는것

for _ in range(n):
    order = input()
    if order == 'R':
        dx, dy = 0, 1
    elif order == 'L':
        dx, dy = 0, -1
    elif order == 'B':
        dx, dy = -1, 0
    elif order == 'T':
        dx, dy = 1, 0
    elif order == 'RT':
        dx, dy = 1, 1
    elif order == 'LT':
        dx, dy = 1, -1
    elif order == 'RB':
        dx, dy = -1, 1
    elif order == 'LB':
        dx, dy = -1, -1

    kx, ky = k[0] + dx, k[1] + dy
    # 옮길 킹자리가 범위 안이고
    if 1<= kx <=8 and 1<= ky <= 8:
        # 1. 킹과 돌과 위치 다르면 킹을 dir대로 바꿔줌.
        if [kx, ky] != r:
            k = [kx, ky]
        # 2. 옮긴 킹과 있던 돌과 위치 같고 돌을 dir대로 옮겼을 때 범위 안이면 돌과 킹을 dir대로 바꿔줌
        elif [kx, ky] == r and 1<= r[0]+dx <=8 and 1<= r[1]+dy <=8:
            k = [kx, ky]
            r = [r[0] + dx, r[1] + dy]

# 킹과 돌의 마지막위치 출력
k[1] = col[k[1]]
r[1] = col[r[1]]
print(*k[::-1], sep='')
print(*r[::-1], sep='')