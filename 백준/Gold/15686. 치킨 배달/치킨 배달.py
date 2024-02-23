import sys
input = sys.stdin.readline

def dfs(ch, lst): # 몇번째 치킨집 판단할지, 유지할 치킨집 리스트
    global mn
    # 가지치기
    if len(lst) > m:
        return
    # 종료조건
    if ch == len(shop):
        if len(lst) == m:
            distance = 0  # 치킨거리
            for ix, iy in house:
                d = 10 ** 5  # 이 집에서 치킨집 최소거리
                for jx, jy in lst:
                    d = min(d, abs(ix - jx) + abs(iy - jy))
                distance += d
            mn = min(mn, distance)
        return
    dfs(ch+1, lst+[shop[ch]])
    dfs(ch+1, lst)

n, m = map(int, input().split()) # m개 치킨집만 남긴다
arr = [list(map(int, input().split())) for _ in range(n)]

house = [] # 집좌표
shop = [] # 치킨집좌표
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            shop.append((i, j))

mn = 10**5 # 치킨거리의 최소값
dfs(0, [])

print(mn)