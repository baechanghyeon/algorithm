t = int(input())

for tc in range(t):
    r_str = int(input())
    str_list = ""

    for i in range(1, r_str+1):
        a, b = input().split()
        str_list += a*int(b)
    cnt = len(str_list)
    if cnt - 10 < 0:
        cnt -= 10
        str_list.insert()


