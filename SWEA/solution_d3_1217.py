for _ in range(10):
    tc = int(input())
    a, b = map(int, input().split())

    def gob(a, b):
        if b == 0:
            return 1
        else:
            return a * gob(a, b-1)

    print('#{} {}'.format(tc, gob(a, b)))
