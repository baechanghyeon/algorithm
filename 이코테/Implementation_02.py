# n = str(input())
#
# result =[]
# cnt = 0
# for i in n:
#     if int(ord(i) >= 97):
#         result.append(str(i))
#     else:
#         cnt += int(i)
#     sorted(result)
#
# print(result+cnt)

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
