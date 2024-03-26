# 10000 * 10000 = 100000000 1억개 5초걸림. 리스트는 안됨
# 세트나 딕셔너리로 하면 10000번만 하면됨
n, m = map(int, input().split())
s_set = {input() for i in range(n)}  # *****

cnt = 0
for i in range(m):
    word = input()
    if word in s_set :
        cnt += 1

print(cnt)