# 1. 2부터 N까지의 모든 자연수를 나열
# 2. 남은 수 중에서 아직 처리하징 않은 가장 작은수를 i 찾는다.
# 3. 남은 수 중에서 i 의배수를 모두 제거 (i는 제거 x)
# 4. 2, 3번을 계속 반복

import math

n = 1000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
# 처음에는 모든 수가 소수인것으로 초기화 ( 0, 1 은 제외)
array = [True for i in range(n + 1)]

# 에라토스테네스의 체 알고리즘 수행
# 2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(math.sqrt(n)) + 1) :
  if array[i] == True : # i가 소수인 경우 ( 남은 수인 경우 )
    # i를 제외한 i의 모든 배수를 지우기
    j = 2
    while i * j <= n :
      array[i * j] = False
      j += 1

for i in range(2, n + 1) :
  if array[i] :
    print(i, end=' ')