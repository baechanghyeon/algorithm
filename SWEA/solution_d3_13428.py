T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result_list = []
    temp = list(str(N))
    result_list.append(N)
    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            if temp[i] == temp[j]:
                continue
            else:
                s = temp[:]
                s[i], s[j] = s[j], s[i]

                if s[0] != '0':
                    s = ''.join(map(str, s))
                    result_list.append(int(s))

    print(f'#{tc} {min(result_list)} {max(result_list)}')