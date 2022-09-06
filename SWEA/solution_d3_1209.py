
for tc in range(1, 11):
    test = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result_num = []
    x1_num = 0
    x2_num = 0
    for i in range(100):
        raw_num = 0
        cal_num = 0
        for j in range(100):
            raw_num += arr[i][j]
            cal_num += arr[j][i]
            if i == j:
                x1_num += arr[i][j]
        result_num.append(raw_num)
        result_num.append(cal_num)

    result_num.append(x1_num)

    for i in range(100):
        x2_num += arr[i][99-i]
    result_num.append(x2_num)

    print(f'#{test} {max(result_num)}')
