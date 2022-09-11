# 팩토리얼 구현 예제

# 반복적으로 구현한 n!
def factorial_iterativbe(n) :
  result = 1
  # 1 부터 n까지의 수를 차례대로 곱하기
  for i in range(1, n+1):
    result *= i
  return result

# 재귀적으로 구현한 n!
def factorial_recuersive(n):
  if n <= 1: # n이 1이하인 경우 1을 반환
    return 1
  # n! = n * (n - 1)!를 그대로 코드로 작성하기
  return n * factorial_recuersive(n - 1)

