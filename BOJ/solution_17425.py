# 시간 초과!
# tc = int(input())
# nums = []
# result = []
# for _ in range(tc):
#     num = int(input())
#     nums.append(num)
#
# for i in range(len(nums)):
#     sum = 0
#     for j in range(1, nums[i]+1):
#         sum += (nums[i]//j) * j
#     result.append(sum)
#
# for k in range(len(nums)):
#     print(result[k])

# 시간 초과!
# tc = int(input())
# for _ in range(tc):
#     num = int(input())
#     sum = 0
#     for i in range(1, num+1):
#         sum += (num//i) * i
#     print(sum)


# 1. N 보다 작거나 같은 모든 자연수는 N의 약수와 약수가 아닌 수로 나눌 수 있다.
# 2. 약수의 개수는 약수가 아닌 수의 개수보다 매우 작다.
# 3. 불필요한 연산을 줄이기 위해 배수를 이용해 약수를 구할 수 있다.

MAX = 1000000
d = [1]*(MAX+1)
s = [0]*(MAX+1)

for i in range(2, MAX+1):
    j = 1
    while i * j <= MAX:
        d[i*j] += i
        j += 1

for i in range(1, MAX+1):
    s[i] = s[i-1] + d[i]

t = int(input())
ans = []

for _ in range(t):
    n = int(input())
    ans.append(s[n])

print('\n'.join(map(str ,ans))+'\n')