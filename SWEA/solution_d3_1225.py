for _ in range(10):
    tc = int(input())
    num_list = list(map(int, input().split()))
    minus = 1
    while num_list[-1] != 0:
        for i in range(1, 6):
            num_list.append(num_list.pop(0) - i)
            if num_list[-1] <= 0:
                num_list[-1] = 0
                break
    print('#{0}'.format(tc), *num_list)
