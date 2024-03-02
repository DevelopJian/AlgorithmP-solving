def dfs(month, price):
    global ans
    # 가지치기
    # 같은레벨(같은 달)에 같은 가격 없을 때만 실행
    if (month, price) in dct:
        return
    else:
        dct[(month,price)] = 1
    if price >= ans :
        return
    # 종료조건
    if month == 13:
        ans = min(ans, price)
        return
    # 함수실행부분
    for _ in range(4):
        if lst[month] * d < m :  # 1일권 가격이 한달권보다 쌀 때만
            dfs(month+1, price + lst[month] * d)# 1일권
        else: # 한달권이 싸거나 같다면
            dfs(month+1, price + m)# 한달권
        if month < 11:
            dfs(month+3, price + m3)# 3달권
        if month == 1:
            dfs(month+12, price + y)# 1년권
 
t = int(input())
for tc in range(1, t+1):
    d,m,m3,y = map(int, input().split())
    lst = [0] + list(map(int, input().split()))
    ans = d * 370
    dct = {} # (달, 가격) : 1
    dfs(1,0)
 
    print(f'#{tc} {ans}')