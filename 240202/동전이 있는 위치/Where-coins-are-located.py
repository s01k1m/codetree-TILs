n, coins = map(int, input().split())

arr = [
    [0] * n
    for _ in range(n)
]

for _ in range(coins):
    x, y = map(int,input().split())
    arr[x-1][y-1] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()