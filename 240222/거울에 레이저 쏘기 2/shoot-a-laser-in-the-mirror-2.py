# 인풋
n = int(input()) # n * n
arr = [
    list(input())
    for _ in range(n)
]
k = int(input())

# 레이저 출발 방향 정하기
directs = [0, 1, 2, 3]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 레이저 출발 방향 n/4 남 n/4 서 n/4 북 n/4 동

if 1 <= k < n:
    start_direct = 0
    s_x = 0
    s_y = k-1
elif n <= k < 2*n:
    start_direct = 1
    s_x = k-n
    s_y = n-1
elif 2*n <= k < 3*n:
    start_direct = 2
    s_x = n-1
    s_y = 3*n-k
else:
    start_direct = 3
    s_x = 4*n-k
    s_y = 0

# 벽 만날때마다 90도로 꺾기 ,, 규칙 찾아야됨..
# 2번이면 남(0)으로 / 서(1) \ 동(3)으로
# 5번이면 서(1)으로 / 남(0)으로 \ 북(2)으로
# 7번이면 북(2)으로 / 동(3)으로 \를 만나면 서(1)로 꺾고
# 10번면 동(3)으로 / 북(2)으로 \ 남(0)으로

mirror = 0

# 레이저의 반사 방향
turning = {
    # 남쪽 방향으로 각 있을때 (/를 만나면, \를 만나면)
    0: (1, 3),
    1: (0, 2),
    2: (3, 1),
    3: (2, 0),
}

# 레이저 발사 시작
x = s_x
y = s_y
direct = start_direct

# # while 레이저가 벽과 만나지 않을때까지
while True:


    # 거울에 부딪혀 튕기는 방향을 찾기
    if arr[x][y] == '/':
        direct = turning[direct][0] 
        mirror += 1
    elif arr[x][y] == '\\':
        direct = turning[direct][1]
        mirror += 1

    # 방향을 찾았으므로 한칸 이동하기
    x = x + dx[direct]
    y = y + dy[direct]
    # 종료 조건
    if x == n or y == n or x == -1 or y == -1:
        break


print(mirror)