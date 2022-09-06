n = int(input())
nums = [int(n) for n in input().split()]

a = max(nums)
b = min(nums)
print(a*b)