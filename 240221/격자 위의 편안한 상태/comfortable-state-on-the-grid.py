N, M = map(int, input().split())

space = [
    [0] * N
    for _ in range(N)
]

arr = [
    tuple(map(int,input().split()))
    for _ in range(M)
]


dxs, dys = [-1, 0, 1, 0],[0, 1, 0, -1]
# 북 동 남 서


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

for _ in arr:
    r, c = _
    r -= 1
    c -= 1

    space[r][c] = 1 # 색칠
    # 편안한지 탐색
    ans = 0

    for i in range(4):
        nr = r + dxs[i]
        nc = c + dys[i]

        if in_range(nr, nc) and space[nr][nc]:
            ans += 1
    
    if ans == 3:
        print(1)
    else:
        print(0)