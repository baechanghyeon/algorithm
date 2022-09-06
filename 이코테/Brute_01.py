# n = int(input())
#
# cnt = 0
# for i in range(3600):
#     if i % 3 == 0:
#         cnt += 1
#
# if n == 3 or n == 13 or n == 23:
#     cnt += 3600
#
# print(cnt)

# 24 * 60 * 60 = 86,400 가지
# 완전 탐색
h = int(input())
cnt = 0
for i in range(1+h):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)

