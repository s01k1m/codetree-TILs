global n
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def get_in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dx, dy = [-1, -1, +1, +1], [+1, -1, -1, +1] # 대각선 탐색
k = n

max_sum = 0

def get_sum(x, y):
    sum = 0
    for idx in range(4):
        for step in range(1, k+1):
            nx = dx[idx] + x
            ny = dy[idx] + y

            if get_in_range(nx, ny):
                x = nx
                y = ny
                sum += grid[x][y]

            else: # 격자 벗어나면 다음 대각선 탐색해야 됨
                break
    
    return sum

for x in range(1, n):
    for y in range(1, n-1):
        max_sum = max(max_sum, get_sum(x, y))

print(max_sum)