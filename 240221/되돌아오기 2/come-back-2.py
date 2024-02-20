# L 90도 회전
# F 바라보는 방향으로 한칸 전진
# 북, 동, 남, 서
dxs, dys = [-1, 0, 1, 0],[0, 1, 0, -1]

arr = list(input())

time = 0

direct = 0

x, y = 0, 0

for _ in arr:
    if _ == "F":
        time += 1
        x += dxs[direct]
        y += dys[direct]

    elif _ == "R":
        time += 1
        direct = (direct + 1) % 4
    elif _ == "L":
        time += 1
        direct = (direct - 1) % 4

    if x == 0 and y == 0:
        break

if x != 0 or y != 0:
    print(-1)
else:
    print(time)