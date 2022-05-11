t = int(input())
for i in range(1, t+1):
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()

    print(f'#1 {" ".join(map(str, n_list))}')
