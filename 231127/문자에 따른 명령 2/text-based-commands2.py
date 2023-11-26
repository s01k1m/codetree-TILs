'''
L 왼쪽 R 오른쪽 F forward
'''

arr = list(input())
# 시계방향 북 동 남 서
dx = [0, 1, 0, -1]
dy = [+1, 0, -1, 0]

cur = 0
x, y = 0,0
for i in arr:
    if i == "L":
        cur -= 1
    if i == "R":
        cur += 1
    if i == "F":
        if cur < 0:
            cur = abs(cur) % 4
            cur = -cur
        cur %= 4
        x, y = x+dx[cur], y+dy[cur]

print(x,y)