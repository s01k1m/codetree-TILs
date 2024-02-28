# LEE
n , m = map(int, input().split())

arr = [
    list(input())
    for _ in range(n)
]

# 위, 아래, 오른, 왼, 대각선 4방향
dx, dy = [0, 0, -1, 1, 1, 1, -1, -1], [-1, 1, 0, 0, 1, -1, -1, 1]

x, y = 0, 0

def in_range(x, y):
    return 0 <= x < n and 0<= y < m

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            for v in range(8):
                nx = i + dx[v]
                ny = j + dy[v]
                if in_range(nx, ny) and in_range(nx+dx[v], ny+dy[v]) and arr[nx][ny] == arr[nx+dx[v]][ny+dy[v]] == "E":
                    ans += 1

print(ans)