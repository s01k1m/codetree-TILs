# 00 / 01 10 / 02 11 20 / 03 12 22 30 / ... / 25 34 / 35
# 4 * 6

row, col = map(int, input().split()) # 3 3
arr = [
    [0] * col
    for _ in range(row)
]
n = 1

for start_col in range(0, col):
    curr_col = start_col
    curr_row = 0

    while 0 <= curr_col < col and 0 <= curr_row < row:
        arr[curr_row][curr_col] = n
        n+=1
        curr_row += 1
        curr_col -= 1

# for j in range(1, col): # 1 2
#     for i in range(col-1, j-1, -1): # 1-> 1 2 2-> 2 
#         # arr[i][j] # 2 1
#         # print(i, col-j)
#         arr[][i] = n
#         n += 1

for start_row in range(1, row):
    curr_row = start_row
    curr_col = col - 1

    while 0 <= curr_col < col  and 0< curr_row < row:
        arr[curr_row][curr_col] = n
        curr_row += 1
        curr_col -= 1
        n += 1
        

for i in range(row):
    for j in range(col):
        print(arr[i][j], end=" ")
    print()