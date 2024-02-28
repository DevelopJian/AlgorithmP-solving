n, l = map(int, input().split()) # 신호등수, 도로길이
road = [0]*(l+1) # 안쓰는 0번째 채워줌
# 도로에 신호등 표시
for _ in range(n):
    d, r, g = map(int, input().split())
    road[d] = (r, g)
# 도로에 시간표시
sec = 0
for i in range(0, l+1):
    if road[i]: # 신호등 있다면
        check = sec % (sum(road[i]))
        if check - road[i][0] < 0: # true면 지금빨간불
            temp = road[i][0] - check
            road[i] = sec + temp
            sec = road[i] + 1
        else:  # 지금 파란불
            road[i] = sec
            sec += 1
    else: # 신호등 없다면
        road[i] = sec
        sec += 1

print(road[-1])