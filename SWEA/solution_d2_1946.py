# t = int(input())
#
# for tc in range(t):
#     r_str = int(input())
#     str_list = ""
#
#     for i in range(1, r_str+1):
#         a, b = input().split()
#         str_list += a*int(b)
#     cnt = len(str_list)
#     if cnt - 10 < 0:
#         cnt -= 10
#         str_list.insert()
#
#

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    text = ''
    for n in range(N):
        alhpa, num = input().split()
        text += alhpa*int(num)
    print('#{}'.format(tc))
    for i in range(1,len(text)+1,10):
        print(text[i-1:i+10-1])