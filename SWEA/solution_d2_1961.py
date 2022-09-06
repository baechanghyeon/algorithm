#             # arr[0][0]
#             arr[i][j] = arr[i+2][j]
#             # arr[0][1]
#             arr[i][j] = arr[i+1][j-1]
#             # arr[0][2]
#             arr[i][j] = arr[i][j-2]
#             # arr[1][0]
#             arr[i][j] = arr[i+1][j+1]
#             # arr[1][1]
#             arr[i][j] = arr[i][j]
T = int(input())


def rotation(a, N):
    new_arr = [[0] * N for _ in range(N)]  # NxN 빈 배열 먼저 만들기
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = a[N - 1 - j][i]
    return new_arr

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    rot_90 = rotation(arr, N)
    rot_180 = rotation(rot_90, N)
    rot_270 = rotation(rot_180, N)

    print(f'#{tc}')
    for i in range(N):
        print("".join(map(str, rot_90[i])), end=' ')
        print("".join(map(str, rot_180[i])), end=' ')
        print("".join(map(str, rot_270[i])), end=' ')
