# T = int(input())
#
# # row, col 인덱스로 탐색할 수 있게 방향 설정 (달팽이 방향이니까 우->하->좌->상)
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
#
# for tc in range(1, T+1):
#     N = int(input())
#     snail = [[0]*N for _ in range(N)]
#     # 초기 위치 & 회전방향 설정
#     r, c = 0, 0
#     dist = 0  # 0:우, 1:하, 2:좌, 3:상
#
#     for n in range(1, N*N + 1):
#         snail[r][c] = n
#         r += dr[dist]
#         c += dc[dist]
#
#         # 범위를 벗어나거나 0이 아닌 다른 값이 이미 있다면, dist 방향 체인지
#         # 근데 이런 경우라면 요소 인덱스를 다시 원위치시켜줘야하므로 빼줘야함
#         # 그런다음 dist의 방향을 바꾸고, 방향 바꿨으면 다시 움직일 수 있도록 행렬 인덱스 업데이트
#         if r < 0 or c < 0 or r >= N or c >= N or snail[r][c] != 0:
#             # 실행취소
#             r -= dr[dist]
#             c -= dc[dist]
#             # dist는 % 4 안해주면 0123, 4567, ... 이런식으로 숫자 커지므로 나머지로 접근
#             dist = (dist + 1) % 4
#             #  다시 gogo
#             r += dr[dist]
#             c += dc[dist]
#
#     print("#{}".format(tc))
#     for row in snail:
#         print(*row)
#     print()
# ================================================================================================================
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     # N * N 의 빈 리스트 생성
#     snail = [[0] * N for _ in range(N)]
#
#     #방향 전환
#     # 우 하 좌 상
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#
#     dist = 0 # 0:우, 1:하, 2:좌:, 3:사에0
#     #초기 좌표
#     x = y = 0
#     snail[x][y] = 1
#
#     for num in range(2, N**2+1):
#         x += dx[dist]
#         y += dy[dist]
#         #배열에 숫자 채우기
#         snail[x][y] = num
#         # 인덱스가 범위 안에 있고, 숫자가 아직 안써졌다면 같은 모드 유지
#         if 0 <= x+dx[dist] < N and 0 <= y + dy[dist] < N and not snail[x+dx[dist][y+dy[dist]]]:
#             continue
#         # 아니라면 dist 변경
#         if dist != 3:
#             dist += 1
#         else:
#             dist = 0
#
#     print(f'#{tc}')
#     for i in snail:
#         print(*i)

# ================================================================================================================
def make_snail(n):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    complete_snail = [[0 for _ in range(n)] for _ in range(n)]

    #0, 0에서 초기화
    cnt = 1
    direction = 0
    x, y = 0, 0
    complete_snail = [x][y] = cnt

    #cnt가 모든 칸에 기록될 때 까지
    while cnt != N**2:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < N and 0<= ny < N and not complete_snail[nx][ny]:
            cnt += 1
            complete_snail[nx][ny] = cnt
            x, y = nx, ny
        else: # 진입 못하면 방향 시계방향 전환
            direction = (direction) % 4

    return complete_snail

for text in range(1, int(input())):
    N = int(input())
    snail = make_snail(N)
    print(f'#{text}')
    for i in range(N):
        print(*snail[i])
