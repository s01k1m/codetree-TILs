row, col = tuple(map(int, input().split()))
arr = [
    [0] * col
    for _ in range(row)
]
cnt = 0
for i in range(col):
    if i % 2 : # 홀수
        for start_row in range(row-1, -1, -1):
            cur_row = start_row
            cur_col = i

            arr[cur_row][cur_col] = cnt
            cnt += 1

    else:
        for start_row in range(row):
            cur_row = start_row
            cur_col = i

            arr[cur_row][cur_col] = cnt
            cnt += 1



for i in range(row):
    for j in range(col):
        print(arr[i][j], end=" ")
    print()