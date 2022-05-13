# t = int(input())
# for tc in range(1, t+1):
#     for input_num in range(9):
#         num = [list(map(int, input().split())) for _ in range(9)]
#         flag = 0
#         for i in range(9):
#             first_num_sum = 0
#             second_num_sum = 0
#             for j in range(9):
#                 first_num_sum += num[i][j]
#                 second_num_sum += num[j][i]
#                 third_num_sum += num[j//3][i//3]
#                 if first_num_sum and second_num_sum == 45:
#                     flag = 1
#                 else:
#                     flag = 0
#
#         #블록
#         for k in range(0, 9, 3):
#             for h in range(0, 9, 3):
#                 third_num_sum = 0
#                 for e in range(3):
#                     for l in range(3):
#                         third_num_sum +=num[e+k][l+h]
#                         if third_num_sum == 45:
#                             flag = 1
#                         else:
#                             flag = 0
#
#         print(f'#{tc} {flag}')

# t = int(input())
# for tc in range(1, t+1):
#     # 스도쿠 판 받아 와서 만들기
#     board = []
#     for _ in range(9):
#         board.append(list(map(int, input().split())))
#
#     answer = 1
#
#     # 3 * 3 작은 격자 9개 만들기
#     square = [[[]for _ in range(3)] for _ in range(3)]
#     for i in range(9):
#         garo = []
#         sero = []
#         for j in range(9):
#             if(board[i][j] in garo) or (board[j][i] in sero) or (board[i][j] in square[i//3][j//3]):
#                 anwer = 0
#                 break
#
#             garo.append(board[i][j])
#             sero.append(board[j][i])
#             square[i//3][j//3].append(board[i][j])
#
#         if not answer:
#             break
#
#     print(f'#{tc} {answer}')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    # 가로 세로 검사
    for i in range(9):
        cnt_r = [0] * 10
        cnt_c = [0] * 10
        for j in range(9):
            cnt_r[arr[i][j]] += 1
            cnt_c[arr[j][i]] += 1

        # 중복 체크
        for k in range(1, 10):
            if cnt_r[k] != 1:
                result = 0
                break
            if cnt_c[k] != 1:
                result = 0
                break

    # 3x3 격자 검사
    for i in range(3):
        for j in range(3):
            cnt_x = [0] * 10
            for k in range(3):
                for l in range(3):
                    cnt_x[arr[3*i+k][3*j+l]] += 1

            for k in range(1, 10):
                if cnt_x[k] != 1:
                    result = 0
                    break

    print("#{} {}".format(tc, result))
