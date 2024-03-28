

t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 원자 수
    atoms = []
    ans = 0
    for _ in range(n):
        x, y, dir, e = map(int, input().split())
        atoms.append([x*2, y*2, dir, e])

    for _ in range(4000): # 최대 4000번 반복
        # atoms가 비면 stop
        if len(atoms) == 0:
            break
        # 이동하기, 범위 넘으면 삭제
        idx = 0
        while idx < len(atoms):
            if atoms[idx][2] == 0:
                atoms[idx][1] += 1
            elif atoms[idx][2] == 1:
                atoms[idx][1] -= 1
            elif atoms[idx][2] == 2:
                atoms[idx][0] -= 1
            elif atoms[idx][2] == 3:
                atoms[idx][0] += 1
            # 현재좌표가 범위 벗어나면 없애기
            if atoms[idx][0] < -2000 or atoms[idx][0] > 2000 or atoms[idx][1] < -2000 or atoms[idx][1] > 2000:
                atoms.pop(idx)
            else:
                idx += 1
        # 정렬 (좌표 중심으로)
        atoms.sort()

        # 좌표 같은거 전부다 터트리기
        poplst = set()
        for row in range(1, len(atoms)):
            if atoms[row][0] == atoms[row-1][0] and atoms[row][1] == atoms[row-1][1]:
                poplst.add(row)
                poplst.add(row-1)
        for row in reversed(sorted(list(poplst))):
            ans += atoms[row][3]
            atoms.pop(row)

    print(f'#{tc} {ans}')