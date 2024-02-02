n = int(input())
arr = [
    [0] * n
    for _ in range (n)
]


for i in range(n):
    arr[i][0] = 1
    arr[0][i] = 1

for row in range(1, n):
    for col in range(1, n):
        arr[row][col] = arr[row][col-1] + arr[row-1][col] + arr[row-1][col-1]

for row in range(0, n):
    for col in range(0, n):
        print(arr[row][col], end=" ")

    print()