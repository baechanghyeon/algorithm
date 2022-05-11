t = int(input())


for tc in range(1, t+1):
    size_num, kill_num = map(int, input().split())
    num_list = [[0]*size_num for k in range(size_num)]
    # 테스트케이스 값 2차원 리스트로 받기
    for i in range(size_num):
        num = list(map(int, input().split()))
        for j in range(size_num):
            num_list[i][j] = num[j]

    max_list = []
    for k in range(size_num - kill_num + 1):
        for h in range(size_num - kill_num + 1):
            kill = 0
            for g in range(kill_num):
                for j in range(kill_num):
                    kill += num_list[g+k][j+h]
            max_list.append(kill)

    print(f'#{tc} {max(max_list)}')










