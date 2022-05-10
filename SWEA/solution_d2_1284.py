T = int(input())

for i in range(1, T+1):
    num = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
            a = a + 1
        elif num % 3 == 0:
            num /= 3
            b = b + 1
        elif num % 5 == 0:
            num /= 5
            c = c + 1
        elif num % 7 == 0:
            num /= 7
            d = d + 1
        elif num % 11 == 0:
            num /= 11
            e = e +1

    print(f'#{i} {a} {b} {c} {d} {e}')