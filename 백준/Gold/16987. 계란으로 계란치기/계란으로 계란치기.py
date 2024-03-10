# 상대계란의 무게만큼 내구도 감소
# 내구도 0되면 깨짐
def dfs(idx, sm, lst): # 계란인덱스, 깨진계란 수, 변경된 내구도 리스트
    global mx
    # 마지막 계란 들었으면 종료
    if idx == n:
        mx = max(sm, mx)
        return
    # 내가 깨져있다면 다음으로 넘기기
    if nae[idx] <= 0:
        dfs(idx + 1, sm, lst)
        return
    # 나는 안깨져있는데(바로 앞에서 리턴 안됨) 다른 계란이 다 깨져있는 경우
    # 아래 for문에서 dfs 안돌아가기 때문에 따로 돌려줘야함
    if sm == n - 1:
        mx = max(sm, mx)
        return
    # 계란 치기
    for i in range(n):
        # i가 내가 아니고, 안깨진 상태일 때 i를 친다
        if i != idx and lst[i] > 0:
            lst[i] -= wt[idx]
            lst[idx] -= wt[i]
            # 깨진 계란 수 세기
            temp = 0
            if lst[i] <= 0:
                temp += 1
            if lst[idx] <= 0:
                temp += 1
            dfs(idx + 1, sm + temp, lst)
            # 원상복구
            lst[i] += wt[idx]
            lst[idx] += wt[i]

n = int(input())
nae = [] # 내구도 리스트
wt = [] # 무게 리스트
for _ in range(n):
    a, b = map(int, input().split())
    nae.append(a)
    wt.append(b)
mx = 0 # 깨진 최대 계란 수
dfs(0, 0, nae)
print(mx)