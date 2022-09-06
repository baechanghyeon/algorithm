# t = int(input())
# string_list =""
# for i in range(1, t+1):
#     string_list += str(i)+" "
#
# string_list = string_list.replace('3', '-')
# string_list = string_list.replace('6', '-')
# string_list = string_list.replace('9', '-')
#
# print(string_list)

t = int(input())
for i in range(1, t+1):
    cnt = 0
    if (i % 10) == 3 or (i % 10) == 6 or (i % 10) == 9:
        cnt += 1
    if (i // 10) != 0 and (i // 10) % 3 == 0:
        cnt += 1

    if cnt >= 1:
        i = '-' * cnt
    print(i, end=' ')

