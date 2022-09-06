# score_result = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
# T, K = map(int, input().split())
# for plus in range(1, T//10):
#     score_result.insert(0, 'A+')
#
# total_list = [0]*100
# for i in range(T):
#     num1, num2, num3 = map(int, input().split())
#     num_score = round(((num1 / 35) + (num2 / 45) + (num3 / 20))*10)
#     total_list[i] = num_score
#
#
# for j in range(1, K+1):
#     K_score = total_list[K-1]
#     total_list.sort()
#     last_num = total_list.index(K_score)
#     K_score_result = total_list.index(K_score)
#     print(K_score_result)
#     print(f'#{j} {score_result[int(K_score_result)]}')
#
# #
#
#

T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1, T+1):
    N, K = map(int, input().split())
    total_list = []
    for _ in range(N):
        mid, final, hws = map(int, input().split())
        total = (mid * 0.35) + (final * 0.45) + (hws * 0.2)
        total_list.append(total)

    # K번 학생 인덱스 구하기
    k_score = total_list[K-1]

    #정렬
    total_list.sort(reverse=True)
    div = N//10
    final_k_score = total_list.index(k_score) // div

    print(f'#{tc} {grades[final_k_score]}')










