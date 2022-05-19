t = int(input())
#
# # num_list 가 충족 될 시 종료
# for tc in range(t):
#     num = int(input())
#     sum = num
#     num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     while len(num_list) != 0:
#         cnt = 0
#         result_num = list(map(int, str(sum)))
#         for i in range(len(num_list)):
#             for j in range(len(result_num)):
#                 if num_list[i] == result_num[j]:
#                     num_list.remove((num_list[i]))
#                 cnt += 1
#                 sum += num


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = [0] * 10
#     # 배수 올리기
#     i = 1
#     # numbers 리스트 안에 0이 없을 시 false
#     while 0 in numbers:
#         num = str(N * i)
#         for j in range(len(num)):
#             numbers[int(num[j])] += 1
#         i += 1
#     print(f'#{tc} {i}')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    zero_to_nine = [str(i) for i in range(10)]

    while zero_to_nine:
        cnt += 1
        room = N * cnt
        room = str(room)
        for i in room:
            if i in zero_to_nine:
                zero_to_nine.remove(i)


    print(f'#{tc} {room}')




