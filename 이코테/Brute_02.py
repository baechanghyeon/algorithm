input_data = input()

row = int(input_data[1]) # 행
column = int(ord(input_data[0])) - int(ord('a'))+1 # 아스키 코드 통해서 변환

# 방향 벡터 정하기 - 나이트가 이동할 수 있는 8가지 방향 정의
steps =[ (-2, -1), (-2, 1), (2, 1), (2, -1), (-1, -2), (-1, 2), (1, -2), (1, 2) ]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인 하는 부분
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
        result +=1

print(result)