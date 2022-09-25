# UnionFind 경로 압축
# 찾기 함수를 재귀적으로 호출 한뒤에 부모 테이블 값을 바로 갱신

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x) :
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x :
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

  