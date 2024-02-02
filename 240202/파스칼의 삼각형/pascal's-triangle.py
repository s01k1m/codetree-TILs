n = int(input())
arr = [
    [0] * n
    for _ in range(n)
]

arr[0][0] = 1

for row in range(1, n):
    for col in range(n):
        arr[row][col] =arr[row-1][col-1] + arr[row-1][col]

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            print(arr[i][j], end= " ")
        else:
            break

    print()