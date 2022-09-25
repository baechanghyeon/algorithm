# 대표적인 최소 신장 트리 알고리즘
# 그리디 알고리즘으로 분류
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생 시키는지 확인
#   1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
#   2) 사이클이 발생하는 경우 최소 신장트리에 포함 시키지 않는다
# 3. 모든 간선에 대해 2번 반복

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x) :
  # 루트 노드를 찾을 때까지 재귀 호출
  if parent[x] != x :
    return find_parent(parent, parent[x])
  return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b ) :
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else :
    parent[a] = b

v, e = map(int, input().split())
parent = [0] * ( v + 1 )

# 모든 간선을 담을 리스트, 최종 비용을 담을 변수
edges = []
result = 0

for i in range(1, v + 1) :
  parent[i] = i

# 모든 간선에 대한 정보 입력 받기
for _ in range(e) :
  a, b, cost = map(int, input().split())
  # 비용 순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
  edges.append((cost, a, b))

edges.sort()

# 간선을 하나씩 확인하며
for edge in edges :
  cost, a, b = edge
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b) :
    union_parent(parent, a, b)
    result += cost

print(result)