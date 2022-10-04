import sys
sys.setrecursionlimit(int(1e5)) # 런타임 오류 피하기
n = int(input())

parent = [0] * ( n + 1 )
d = [0] * (n + 1)
c = [0] * (n + 1)
graph = ([] for _ in range(n + 1)) 

for _ in range(n - 1) :
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# 루트 노드부터 시작하여 깊이를 구하는 함수
def dfs(x, depth) :
  c[x] = True
  d[x] = depth
  for y in graph[x] :
    if c[y] :
      continue
    parent[y] = x
    dfs(y, depth + 1)

# A 와 B의 최소 공통 조상을 찾는 함수
def lca(a, b ) :
  # 깊이를 동일하게
  while d[a] != d[b] :
    if d[a] > d[b] :
      a = parent[a]
    else :
      b = parent[b]
  while a != b :
    a = parent[a]
    b = parent[b]
  return a

dfs(1, 0)

m = int(input())
for i in range(m) :
  a, b = map(int, input().split())
  print(lca(a, b))