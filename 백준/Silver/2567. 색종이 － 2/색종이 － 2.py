# 겉 직사각형 둘레 + 안직사각형둘레

n = int(input())

# 0으로된 이차원배열
# 색종이부분 1로 다 바꾸기
# 겉에있는 1 갯수구하기 (사방에 0 있는 갯수구하기)

arr = [[0]*102 for _ in range(102)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                if arr[i+dx][j+dy] == 0:
                    cnt += 1
print(cnt)