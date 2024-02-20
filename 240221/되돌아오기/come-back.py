n = int(input())

time = 0

sx = 0
sy = 0

x = sx
y = sy

directs = {
    "W": 0,
    "S": 1,
    "N": 2,
    "E": 3,
}

dx, dy = [0, 1, -1, 0], [-1, 0, 0, 1]

for _ in range(n):
    d, s = input().split()

    direct = directs[d]
    for _ in range(int(s)):
        time += 1
        x = dx[direct] + x
        y = dy[direct] + y

        if x == 0 and y == 0:
            break

    if x == 0 and y == 0:
        break

print(time)