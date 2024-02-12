def square(a, b, c, d, e):
    for x in range(a, c):
        for y in range(b, d):
            arr[x][y] += e


arr = [[0] * 2001 for _ in range(2001)]
offset = 1000

x1, y1, x2, y2 = map(int, input().split())
square(x1+offset, y1+offset, x2+offset, y2+offset, 1)

x3, y3, x4, y4 = map(int, input().split())
square(x3+offset, y3+offset, x4+offset, y4+offset, -2)

horizontal = []
vertical = []

for i in range(x1+offset, x2+offset):
    for j in range(y1+offset, y2+offset):
        if arr[i][j] == 1:
            horizontal.append(i)
            vertical.append(j)

if len(horizontal) > 0:
    x = max(horizontal)+1 - min(horizontal)
    y = max(vertical)+1 - min(vertical)
    print(x*y)
else:
    print(0)