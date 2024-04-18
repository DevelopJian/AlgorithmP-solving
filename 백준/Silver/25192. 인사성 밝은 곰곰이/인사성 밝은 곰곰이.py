n = int(input())

ans = turn = 0
dct = {}
for _ in range(n):
    word = input()
    if word == 'ENTER':
        turn += 1
    else:
        if word not in dct:
            dct[word] = [turn]
            ans += 1
        else:
            if turn not in dct[word]:
                dct[word].append(turn)
                ans += 1

print(ans)
