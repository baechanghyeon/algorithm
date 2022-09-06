T = int(input())

for tc in range(1, T+1):
    input_str = input()
    flag = 0
    new_str = ""
    for i in range(len(input_str)-1, -1, -1):
        new_str += input_str[i]
    if input_str == new_str:
        flag = 1
    else: flag = 0

    print(f'#{tc} {flag}')

