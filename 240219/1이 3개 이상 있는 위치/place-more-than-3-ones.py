n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0] # 동 북 서 남

def in_range(x, y): # 범위 유효성 검사
    return 0 <= x <= n-1 and 0 <= y <= n-1


cnt = 0
for i in range(n):
    for j in range(n):
        near = 0


        for dx, dy in zip(dxs, dys):

            nx, ny = i+dx, j+dy
            if in_range(nx, ny) and arr[nx][ny] == 1:
                near += 1

            
        if near >= 3:
            cnt += 1
            continue

print(cnt)