tc = int(input())
num = []

for i in range(tc):
    tcm = int(input())
    # 1000명의 학생의 점수 받기
    num = list(map(int, input().split()))
    # 1000명의 학생 점수가 0 ~ 100점까지 점수 갯수 구하기
    num_cnt_list = []
    for j in range(100):
        num_cnt_list.append(num.count(j))
    max_list_index = list(filter(lambda  x: num_cnt_list[x] == max(num_cnt_list), range(len(num_cnt_list))))

    print(f'#{tcm} {max(max_list_index)}')


