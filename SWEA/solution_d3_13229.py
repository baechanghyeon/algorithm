T = int(input())

for tc in range(1, T+1):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    day = str(input())
    day_index = days.index(day)
    result = 7 - day_index
    print(f'#{tc} {result}')