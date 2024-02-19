max_step = 100
max_order = 1000

arr = [0] * (max_order * max_step * 2 + 1)
color = [0] * (max_order * max_step * 2 + 1)
n = int(input())
cur = 1000
for _ in range(n):
    step, direction = input().split()
    step = int(step)
    if direction == "R":
        nxt = cur + step

        for i in range(cur, nxt, +1):

            arr[i] += 1
            color[i] = "B"

        cur = nxt - 1

    elif direction == "L":
        nxt = cur - step

        for i in range(cur, nxt, -1):
            arr[i] += 1
            color[i] = "W"
        
        cur = nxt +1


gray = 0
white = 0
black = 0  
for e in range(len(color)):
    if arr[e] == 0:
        continue
    elif arr[e] >= 4:
        gray += 1
    elif color[e] == "W":
        white += 1
    elif color[e] == "B" :
        black += 1


print(white, black, gray)