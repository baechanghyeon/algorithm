m = int(input())
n = list(map(int, input().split()))

n.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in n:
    count += 1 # 현재 그룹에 해당 모험가를 포함
    if count >= i:
        result += 1
        count = 0

print(result)
