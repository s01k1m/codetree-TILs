# x, y 
# max_x, max_y를 하고 이거의 곱만큼의 완전탐색을 진행
# 1사분면 2, 3, 4을 어떻게 파악하지?
# (a, b)
# 1사분면 quadrant a > x, b > y 
# 2사분면 a < x, b > y
# 3사분면 a < x, b < y
# 3사분면 a > x, b < y
import sys


def devide(i, j, tempx, tempy):
    global quadrant1, quadrant2, quadrant3, quadrant4

    if tempx > i and tempx > j:
         quadrant1 += 1
    elif tempx < i and tempx > j:
         quadrant2 += 1
    elif tempx < i and tempx < j:
         quadrant3 += 1
    elif tempx > i and tempx < j:
         quadrant4 += 1

def compare(a, b, c, d):
    l = [a,b,c,d]
    return max(l) - min(l)

n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

points.sort(key=lambda x:x[0])

min_x = points[0][0]
max_x = points[-1][0]

points.sort(key=lambda x:x[1])

min_y = points[0][1]
max_y = points[-1][1]


init = 100
ans = 0

for i in range (min_x, max_x + 1):
    for j in range(min_y, max_y + 1):

        quadrant1 = 0
        quadrant2 = 0
        quadrant3 = 0
        quadrant4 = 0 

        for a, b in points:
            devide(i, j, a, b)

        temp = compare(quadrant1, quadrant2, quadrant3, quadrant4)
        if init > temp:
            init = temp
            ans = max(quadrant1, quadrant2, quadrant3, quadrant4)

print(ans)