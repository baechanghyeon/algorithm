
for _ in range(10):
    cnt = 0
    num_round = int(input())
    check_str = str(input())
    str_list = str(input())
    for i in range(len(str_list)-len(check_str)+1):
        plus_str = []
        for j in range(len(check_str)):
            plus_str.append(str_list[i+j])
        result_str = "".join(plus_str)
        if result_str == check_str:
            cnt += 1

    print(f'#{num_round} {cnt}')
