offset = 100
n = int(input())

area = [[0]*201 for _ in range(201)]

def area_rectangle(a, b, c, d):
    for x in range(a, c):
        for y in range(b, d):
            area[x][y] = 1

for _ in range(n):

    x1, y1, x2, y2 = map(int, input().split())
    area_rectangle( x1+offset, y1+offset, x2+offset, y2+ offset)

answer = 0
for i in area:
    answer+=sum(i)
print(answer)