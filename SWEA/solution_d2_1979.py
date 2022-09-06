t = int(input())

for tc in range(1, t+1):
     n, k = map(int, input().split())
     arr = [list(map(int, input().split())) for _ in range(n)]
     # 가로 검사
     ans = 0
     for i in range(n):
         s_cnt = 0
         for j in range(n):
             if arr[i][j] == 1:
                s_cnt += 1
             if arr[i][j] == 0 or j == n-1:
                if s_cnt == k:
                   ans += 1
                s_cnt = 0
     # 세로 검사
         for j in range(n):
             if arr[j][i] == 1:
                 s_cnt += 1
             if arr[j][i] == 0 or j == n - 1:
                 if s_cnt == k:
                     ans += 1
                 s_cnt = 0

     print(f'#{tc} {ans}')


