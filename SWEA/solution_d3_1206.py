T = 10
for tc in range(1, 11):
    building_length = int(input())
    building = list(map(int, input().split()))
    result = 0
    for i in range(2, building_length-2):
        max_num = []
        max_num.append(building[i-2])
        max_num.append(building[i-1])
        max_num.append(building[i+1])
        max_num.append(building[i+2])
        if building[i] > max(max_num):
            result += building[i] - max(max_num)
    print(f'#{tc} {result}')
