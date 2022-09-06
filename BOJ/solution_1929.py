# 시간 초과!
# for i in range(a, b+1):
#     cnt = 0
#     if(i == 1):
#         continue;
#     for j in range(2, i+1):
#         if(i%j == 0):
#             cnt += 1
#     if(cnt == 1):
#         print(i)

# 소수 탐색 시 범위를 제곱으로 하여 계산
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

a, b = map (int, input().split())

for j in range(a, b+1):
    if isPrime(j):
        print(j)




