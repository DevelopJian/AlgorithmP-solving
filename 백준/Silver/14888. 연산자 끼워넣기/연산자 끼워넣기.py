# 시간복잡도 : 4**10 = 2**20 -> 가능

def dfs(idx, result, add, sub, mul, div): # 계산할 뒤의 값 인덱스, 이전계산결과, 연산자 남은수
    global mx, mn
    # 가지치기
    if -10**9 > result or result > 10**9:
        return
    # 종료조건
    if idx == n:
        mx = max(mx, result)
        mn = min(mn, result)
        return
    # 연산하기
    if add > 0:
        dfs(idx + 1, result + arr[idx], add-1, sub, mul, div)
    if sub > 0:
        dfs(idx + 1, result - arr[idx], add, sub-1, mul, div)
    if mul > 0:
        dfs(idx + 1, result * arr[idx], add, sub, mul-1, div)
    if div > 0:
        dfs(idx + 1, int(result/arr[idx]), add, sub, mul, div-1)

n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
mx, mn = -10**9, 10**9
dfs(1, arr[0], add, sub, mul, div)
print(mx)
print(mn)