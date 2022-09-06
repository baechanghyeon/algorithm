T = int(input())
num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1, T+1):
    tc_num, str_length = map(str, input().split())
    str_list = list(map(str, input().split()))
    num_check_list = []
    for i in range(int(str_length)):
        num_check_list.append(num_list.index(str_list[i]))
    num_check_list.sort()
    num_result = []
    for j in range(int(str_length)):
        num_result.append(num_list[num_check_list[j]])

    print(f'{tc_num} {" ".join(num_result)}')


