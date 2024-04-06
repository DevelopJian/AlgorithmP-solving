from collections import deque

n, k = map(int, input().split()) # n = 컨베이어 길이, 내구도 0인것 k개 이상이면 모두 종료
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)

cnt, ans = 0, 0 # 내구도, 단계
while True:
    ans += 1
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0 # 마지막자리 로봇 없애주기
    for i in range(n-2, -1, -1):
        # 로봇 옯기기 : 1. 나한테 로봇있고 2. 우측 내구도 0보다 크고 2. 우측에 로봇 있다면
        if robot[i] == 1:
            if belt[i+1] > 0 and robot[i+1] == 0:
                belt[i+1] -= 1
                robot[i+1] = 1
                robot[i] = 0
    robot[-1] = 0 # 마지막자리 로봇 없애주기
    if belt[0] > 0: # 첫번째 자리 로봇 올려주기
        robot[0] = 1
        belt[0] -= 1
    if belt.count(0) >= k:
        break
print(ans)