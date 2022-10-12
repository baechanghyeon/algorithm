# 1) 모든 간선이 양수인 경우
# 2) 음수 간선이 있는 경우
#  1. 음수 간선 순환은 없는 경우
#  2. 음수 간선 순환이 있는 경우
# 벨만 포드 알고리즘 
# 1. 출발 노드 설정
# 2. 최단 거리 테이블을 초기화
# 3. 다음의 과정을 N - 1 번 반복
#   1. 전체 간선 E개를 하나씩 확인한다.
#   2. 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
# 만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번의 과정을 한번 더 수행
# 이때 최단 거리 테이블이 갱신된다면 음수 간선 순환이 존재하는 것

import sys
input = sys.stdin.readline
INF = int(1e9) 

def bf(start) :
  dist[start] = 0

  for i in range(n) :
    for j in range(m) :
      cur = edges[j][0]
      next_node = edges[j][1]
      cost = edges[j][2]
      # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if dist[cur] != INF and dis[next_node] > dist[cur] + cost :
        dist[next_node] = dist[cur] + cost
        # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
        if i == n - 1 :
          return True
  return False

# 노드의 개수, 간선의 개수를 입력 받기
n, m = map(int, input().split())
edges = []
dist = [INF] * (n + 1)

for _ in range(m) :
  a, b, c = map(int, input().split())
  edges.append((a, b, c))

# 벨만 포드 알고리즘을 수행
negative_cycle = bf(1) # 1번 노드 시작

if negative_cycle :
  print('-1')
else :
  for i in range(2, n + 1) :
    if dist[i] == INF :
      print('-1')
    else :
      print(dist[i])
      