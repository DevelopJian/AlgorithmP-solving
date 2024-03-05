from collections import deque

def bfs():
    q = deque([(0, 0, arr[0][0])]) # (이전좌표 행, 열, 지나온알파벳문자열)
    v = [[set() for _ in range(c)] for _ in range(r)]
    v[0][0].add(arr[0][0])
    ans = 0

    while q:
        x, y, string = q.popleft()
        # 정답처리
        ans = max(ans, len(string))

        for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            # 1. 범위 2. 중복값 아닌경우, 중복 시퀀스 아닌 경우(같은 좌표에 있더라도 지나온 길에 따라 뒤의 결과 달라짐)
            if 0<= nx <r and 0<= ny <c and arr[nx][ny] not in string\
                    and (string + arr[nx][ny] not in v[nx][ny]):
                v[nx][ny].add(string + arr[nx][ny])   # 왜 괄호 한번 더치지?
                q.append((nx, ny, string + arr[nx][ny]))
    return ans

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

print(bfs())