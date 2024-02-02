n = int(input())

arr = [
    [0] * n
    for _ in range(n)
]

x = n % 2
cnt = 1
for start_col in range(n, 0, -1):
    if start_col % 2 == x:
        for start_row in range(n, 0, -1):

            # arr[start_row][start_col] = n
            arr[start_row-1][start_col-1] = cnt
            cnt += 1
    else:
        for start_row in range(0, n):
            arr[start_row][start_col-1] = cnt
            cnt += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()