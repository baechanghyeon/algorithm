t = int(input())

nums = list(map(int, input().split()))
nums.sort()

result = 0
cnt = 0
for i in nums:
    cnt += i
    result += cnt
print(result)