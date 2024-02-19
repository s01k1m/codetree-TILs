max_step = 100
max_order = 1000

class Tile:
    def __init__(self, last_color = ""):
        self.last_color = last_color
        self.cnt_w = 0
        self.cnt_b = 0

    def white(self):
        self.cnt_w += 1

    def black(self):
        self.cnt_b += 1
    
    def w(self):
        return self.cnt_w

    def b(self):
        return self.cnt_b

color = list( Tile() for _ in range(max_order * max_step * 2 + 1))

n = int(input())
cur = 1000
segments = []

for _ in range(n):
    step, direction = input().split()
    step = int(step)

    if direction == "R":
        nxt = cur + step - 1 # 현재 자리를 칠한다는 것을 반영함 즉 한칸 덜감
        segments.append((cur, nxt + 1, "B")) # +1은 위에서 현재를 포함하는 바람에 한 것임

        cur = nxt

    elif direction == "L":
        nxt = cur - step + 1 # 현재 자리를 칠한다는 것을 반영함
        segments.append((nxt, cur + 1, "W"))

        cur = nxt

for x, y, c in segments:
    for i in range(x, y):
        if c == "B":
            color[i].last_color = "B"
            color[i].black()
        else:
            color[i].white()
            color[i].last_color = "W"

gray = 0
white = 0
black = 0

for e in range(len(color)):
    # break 
    l_w = color[e].w()
    l_b = color[e].b()

    if color[e].last_color == "":
        continue
    elif l_b >= 2 and l_w >= 2:
        gray += 1
    elif color[e].last_color == "W":
        white += 1
    elif color[e].last_color == "B" :
        black += 1


print(white, black, gray)