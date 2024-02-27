t = int(input())
for tc in range(1, t+1):
    st = input()
    arr = [[] for _ in range(4)]
    dct = {'S' : 0, 'D' : 1, 'H' : 2, 'C' : 3}

    for i in range(0, len(st), 3):
        arr[dct[st[i]]].append(int(st[i+1:i+3]))

    ans = []
    for lst in arr:
        if len(lst) != len(set(lst)):
            print(f'#{tc} ERROR')
            break
        ans.append(13 - len(lst))
    else:
        print(f'#{tc}', *ans)