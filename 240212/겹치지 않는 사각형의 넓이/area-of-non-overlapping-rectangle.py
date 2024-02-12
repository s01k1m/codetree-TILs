arr =[[0] * 2001 for _ in range(2001)]

def square(a,b,c,d,e):
    for x in range(a, c):
        for y in range(b, d):
            arr[x][y] += e


for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    # print(x1+1000, y1+1000, x2+1000, y2+1000)
    square(x1+1000, y1+1000, x2+1000, y2+1000, 1)

for _ in range(1):
    x1, y1, x2, y2 = map(int, input().split())
    square(x1+1000, y1+1000, x2+1000, y2+1000, -3)
ans= 0

for x in range(2001):
    for y in range(2001):
        if 1 <= arr[x][y] < 3:
            ans += 1

print(ans)