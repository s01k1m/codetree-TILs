n , m = map(int, input().split())

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

d = 0

arr = [
    [0] * m 
    for _ in range(n)
]

x, y  = 0, 0

text = 65
cnt = 1

while cnt <= n * m:
    if 0 <= x < n and 0 <= y < m and arr[x][y] == 0:
        arr[x][y] = chr(text)
        text += 1
        cnt += 1

    if text > 90:
        text = 65

    nx = x + dxs[d]
    ny = y + dys[d]

    if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != 0:
        d += 1
        d %= 4
    
    x = x + dxs[d]
    y = y + dys[d]

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()