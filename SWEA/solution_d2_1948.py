T = int(input())
d_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    sum = 0

    if m1 != m2 :
        sum = (d_list[m1] - d1) + (d_list[m2] - (d_list[m2] - d2))
        for i in range(m2-m1-1):
            sum += d_list[m1+i+1]
    else:
        sum = d2-d1
    sum += 1

    print(f'#{tc} {sum}')
