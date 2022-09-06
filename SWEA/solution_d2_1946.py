t = int(input())
for tc in range(1,t+1):
    alpha = int(input())
    result =""
    #문자 갯수 만큼 문자열에 더하기
    for x in range(alpha):
        a, b = input().split()
        result += a * int(b)
    # 10칸마다 줄바꿈
    point=""
    for i in range(len(result)//10+1):
        point += result[i*10:(i+1)*10] + "\n"
    delete = point[:-1]
    print(f'#{tc}\n{delete}')