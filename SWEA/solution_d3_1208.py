for tc in range(1, 11):
    dump = int(input())
    num_list = list(map(int, input().split()))
    for _ in range(dump):
        num_list[num_list.index(max(num_list))] -= 1
        num_list[num_list.index(min(num_list))] += 1

    result = max(num_list) - min(num_list)
    print(f'#{tc} {result}')