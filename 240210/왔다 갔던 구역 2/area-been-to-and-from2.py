OFFSET = 1000
MAX_R = 2000

# 변수 선언 및 입력
n = int(input())
segments = [
    tuple(input().split())
    for _ in range(n)
]

checked = [0] * (MAX_R + 1)
cur = 1000
for move, direction in segments:
    move = int(move)
    # 구간을 칠해줍니다.
    # 구간 단위로 진행하는 문제이므로
    # next에 +1가 들어가지 않음에 유의합니다.
    if direction == "R":
        next = cur + move
        for i in range(cur, next):
            checked[i] += 1
        cur = next

    elif direction == "L":
        next = cur - move
        for i in range(next, cur):
            checked[(i)] += 1
        cur = next

# 2번 이상 지나간 영역의 크기

answer = 0
for i in checked:
    if i >= 2:
        answer += 1

print(answer)