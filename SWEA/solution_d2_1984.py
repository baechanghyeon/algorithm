# T = int(input())

# for i in range(1, T+1):
#     num = list(map(int, input().split(' ')))
#     num.remove(max(num))
#     num.remove(min(num))
#     total = sum(num)/8
#     print(f'#{i} {round(total)}')


# T = int(input())

# for i in range(1, T+1):
#     num = list(map(int, input().split(' ')))
#     num.sort()
#     max_num = num[-1]
#     min_num = num[0]
#     num.remove(max_num)
#     num.remove(min_num)
#     total = sum(num)/8
    
#     print(f'#{i} {round(total)}')


T = int(input())

for i in range(1, T+1):
    num = list(map(int, input().split()))
    num.sort()
    max_num = num[-1]
    min_num = num[0]
    num.remove(max_num)
    num.remove(min_num)
    total = sum(num)/8
    
    print(f'#{i} {round(total)}')