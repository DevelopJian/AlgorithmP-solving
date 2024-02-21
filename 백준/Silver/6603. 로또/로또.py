def dfs(cnt, start, subset): # 번호고른갯수, 몇번부터 골라야하는지, 만들고있는집합
    # 종료조건
    if cnt == 6:
        subset_lst.append(subset)
        return
    if start <= k:
        for idx in range(start, k): # idx = arr의 인덱스
            # arr[idx]를 subset에 넣는다
            dfs(cnt+1, idx+1, subset+[arr[idx]])

while True:
    arr = list(map(int, input().split()))
    if arr == [0]:
        break
    else:
        k = arr[0] # 집합원소갯수
        arr = arr[1:]  # 0~(k-1)
        # 번호 6개를 골라야함 다중트리 1 -> 6번까지
        subset_lst = []

        dfs(0, 0, [])
        for lst in subset_lst:
            print(*lst)
    print()
