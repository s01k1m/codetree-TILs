n = int(input())

global history
history = {} # 딕셔너리에 {장소 : 방문횟수}를 저장할거임

def visit(x):
    try: 
        n = history[x] + 1
        history[x] = n
    except KeyError: # 딕셔너리에 장소를 키로 조회했을때 없으면 에러나서 에러 처리해줘야됨.
        history[x] = 1

cur = 0

for _ in range(n):
    move, direction = input().split()
    move = int(move)

    if direction == "R":
        next = cur + move
        for i in range(cur, next):
            visit(i)
        
        cur = next

    elif direction == "L":
        next = cur - move
        for i in range(cur, next, -1):
            visit(i)

        cur = next

answer = 0
for key, value in history.items():
    if value > 1:
        answer += 1

print(answer)