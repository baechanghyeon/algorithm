T = int(input())
for tc in range(1, T+1):
    N = int(input())
    R = N//2
    num_list = [list(map(int, input())) for _ in range(N)]
    start, end = N//2, N//2
    result = 0
    for i in range(N):
        for j in range(start, end+1):
            result += num_list[i][j]

        if i < N//2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print(f'{tc} {result}')












