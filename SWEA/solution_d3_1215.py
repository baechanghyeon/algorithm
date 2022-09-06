
for tc in range(1, 11):
    alpha_lg = int(input())
    alpha_list = [str(input()) for _ in range(8)]
    cnt = 0

    for i in range(8):
        for j in range(9-alpha_lg):
            raw_check_list = []
            cal_check_list = []
            for k in range(alpha_lg):
                raw_check_list.append(alpha_list[i][j+k])
                cal_check_list.append(alpha_list[j+k][i])
            raw_check_str = "".join(raw_check_list)
            cal_check_str = "".join(cal_check_list)
            raw_reverse_list = []
            cal_reverse_list = []
            for m in range(alpha_lg):
                raw_reverse_list.append(raw_check_str[alpha_lg-m-1])
                cal_reverse_list.append(cal_check_str[alpha_lg-m-1])
            raw_reverse_str ="".join(raw_reverse_list)
            cal_reverse_str ="".join(cal_reverse_list)

            if raw_check_str == raw_reverse_str:
                cnt += 1

            if cal_check_str == cal_reverse_str:
                cnt += 1

    print(f'#{tc} {cnt}')



