# 백트래킹 -> 이진트리 형식이 젤 좋음.
# 백트리킹 -> DFS랑 다르게 조건 안맞는 것은 안감

def dfs(subset_len, subset):  # m은 변하지 않으니 줄 필요 없음 # start = 추가한 원소 수
    # 1. 종료조건 + 정답처리 (n과 관련된 것으로 -> 보통은 start를 발전시키다가 종료시키도록)
    if subset_len == m:  # m개의 수열을 완성한 경우
        result.append(subset)
        return
    # 2. 하부단계(함수) 호출
    for element in range(1, n+1): # 1~n까지 선택
        if not visit[element]:  # 선택하지 않은 숫자의 경우 추가
            visit[element] = 1  # 재귀호출하는 곳에서는 visit 1이도록 만들기
            dfs(subset_len + 1, subset + [element])  # 다음 함수에서 start += 1 해주는것임
            visit[element] = 0  # 담번에 다른 함수호출에서 다시 쓰기위해 리셋

n, m = map(int, input().split())
result = [] # 정답을 저장할 리스트
visit = [0] * (n+1) # 중복확인. 0번째 인덱스 안씀

dfs(0, [])

for lst in result:
    print(*lst)