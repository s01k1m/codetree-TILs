x, y = 0, 0

def move(d, step):
    global x
    global y
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for _ in range(step):
        if d == "N":
            x, y = x + dx[0] , y + dy[0]
        elif d == "E":
            x, y = x + dx[1] , y + dy[1]
        elif d == "S":
            x, y = x + dx[2] , y + dy[2]
        elif d == "W":
            x, y = x + dx[3] , y + dy[3]

n = int(input())
for _ in range(n):
    d, step = input().split()
    step = int(step)

    move(d, step)

print(x, y)