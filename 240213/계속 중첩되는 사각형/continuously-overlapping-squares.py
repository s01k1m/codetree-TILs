# 홀 => 레드 짝 => 블루

n = int(input())

arr= [[0]*201 for _ in range(201)] 

def square(a, b, c, d, n):
    offset = 100
    for x in range(a+offset, c+offset):
        for y in range(b+offset, d+offset):
            if n % 2 == 1:
                arr[x][y] = "R"
            elif n % 2 == 0:
                arr[x][y] = "B"


for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    square(x1, y1, x2, y2, _+1)

ans= 0

for x in range(0, 201):
    for y in range(0, 201):
        if arr[x][y]== "B":
            ans += 1
print(ans)