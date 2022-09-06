
# T = int(input())
#
# won_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# for i in range(1, T+1):
#     num = int(input())
#     won_total = [0] * 8
#     won_num = 0
#     won_cnt = 0
#     while num != 0:
#         if num - won_list[won_num] > 0:
#             num = num % won_list[won_num]
#             won_cnt = won_cnt + 1
#         elif num - won_list[won_num] < 0:
#             won_num = won_num + 1
#             won_total.append(won_cnt)
#             won_cnt = 0
#
#     print(f'#{i}')
#     print(*won_total)


# T = int(input())
# for i in range(1, T+1):
#     num = int(input())
#     a = 0
#     b = 0
#     c = 0
#     d = 0
#     e = 0
#     f = 0
#     g = 0
#     h = 0
#     while num != 0:
#         if num-50000 > 0:
#             num -= 50000
#             a += 1
#         elif num-10000 > 0:
#             num -= 10000
#             b += 1
#         elif num-5000 > 0:
#             num -= 5000
#             c += 1
#         elif num-1000 > 0:
#             num -= 1000
#             d += 1
#         elif num-500 > 0:
#             num -= 500
#             e += 1
#         elif num-100 > 0:
#             num -= 100
#             f += 1
#         elif num-50 > 0:
#             num -= 50
#             g += 1
#         elif num-10 > 0:
#             num -= 10
#             h += 1
#     print(f'#{i} {a} {b} {c} {d} {e} {f} {g} {h}')


T = int(input())

won_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for i in range(1, T+1):
    num = int(input())
    won_total = [0] * 8
    for j in range(8):
        if num//won_list[j] != 0:
            won_total[j] = num//won_list[j]
            num = num % won_list[j]

    print(f'#{i} ')
    print(*won_total)
