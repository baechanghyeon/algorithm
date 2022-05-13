t = int(input())

for tc in range(1, t+1):
    a, b, c, d = map(int, input().split())
    hour = a + c
    minutes = b + d
    if hour > 12:
        hour = hour % 12
    if minutes > 60:
        hour = hour + 1
        minutes = minutes % 60

    print(f'#{tc} {hour} {minutes}')