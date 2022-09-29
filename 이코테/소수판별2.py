import math

def is_prime_number(x) :
  # 2부터 x의 제곱근까지의 모든 수를 확인하며
  for i in range(2, int(math.sqrt(x)) + 1) :
    if x % i == 0:
      return False
  return True

print(is_prime_number(4))
print(is_prime_number(7))

# 2부터 x의 제곱근까지의 모든 자연수에 대하여 연산을 수행 
# 2 ~ x 까지 for 문을 돌리는 알고리즘 시간복잡도의 1/2 단축
