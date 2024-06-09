from collections import deque

# 전역 변수 선언
n = 0
m = 0

def solution(maps):
    global n, m  # 전역 변수 사용 선언
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque()

    q.append((0, 0))
    visited[0][0] = True
    
    # 남 동 북 서
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # visited[ny][nx]와 maps[ny][nx]를 사용해야 합니다.
            if area(ny, nx) and not visited[ny][nx] and maps[ny][nx] == 1:
                visited[ny][nx] = True
                q.append((nx, ny))
                maps[ny][nx] = maps[y][x] + 1
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]

def area(x, y):
    global m, n  # 전역 변수 사용 선언
    return 0 <= x < n and 0 <= y < m
