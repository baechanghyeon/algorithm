# 연속적으로 나열된 N개의 수가 있을 때 특정 구간의 모든 수를 합한 값을 계산하는 문제
# 접두사 합 (Prefix Sum) : 배열의 맨앞부터 특정 위치까지의 합을 미리 구해 놓은 것

# 데이터의 개수 N과 데이터 입력 받기
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data :
  sum_value += i
  prefix_sum.append(sum_value)

# 구간 합 계산 ( 세번째 수부터 네 번째 수 까지 )
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])