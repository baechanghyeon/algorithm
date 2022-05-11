tc = int(input())

for i in range(1, tc+1):
    n_len, m_len = map(int, input().split())
    n = list(map(int, input().split()))
    m = list(map(int, input().split()))
    num_result = []
    max_num = max(m_len, n_len)
    min_num = min(m_len, n_len)

    # 이동 횟수 for 문
    for j in range((max_num-min_num) + 1):
        result = 0
        # 이동 할때 마다 곱하고 더한 값
        for k in range(min_num):
            # m_len 이 더 길 때
            if max_num == m_len:
                result = result + (m[j+k] * n[k])
            # n_len 이 더 길 때
            else:
                result = result + (n[j+k] * m[k])
        num_result.append(result)

    print(f'#{i} {max(num_result)}')











