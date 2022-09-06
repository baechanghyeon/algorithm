T = int(input())

for tc in range(1, T+1):
    # a, b = map(str, input().split())
    # if len(a) and len(b) < 2:
    #     result = int(a) * int(b)
    # else:
    #     result = -1
    # print(f'#{tc} {result}')

    a, b = map(int, input().split())
    if 1<= a <=9 and 1<= b <= 9:
        result = a * b
    else:
        result = -1
    print(f'#{tc} {result}')
