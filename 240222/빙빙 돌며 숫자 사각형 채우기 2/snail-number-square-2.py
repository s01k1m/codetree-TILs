# 남 동 북 서 
n, m = map(int, input().split())

arr = [
    [0] * m
    for _ in range(n)
]


dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

d = 0
x = 0
y = 0

cnt = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


while True:
    if in_range(x,y) and arr[x][y] == 0:
        arr[x][y] = cnt
        cnt += 1

    if not in_range(x + dxs[d], y + dys[d]) or arr[x + dxs[d]][y + dys[d]] != 0:
        d += 1
        d %= 4

    x = x+ dxs[d]
    y = y+ dys[d]

    if cnt == n*m +1:
        break



for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()