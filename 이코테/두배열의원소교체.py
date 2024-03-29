n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()  # 배열 a는 오름차순 정렬 수행
a.sort(reverse=True)

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k 번 비교
for i in range(k):
    # a 의 원소가 b의 원소보다 작은 경우
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:  # a의 원소가 b의 원소 보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))
