import sys

n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

# 시계 반대방향..
min_move = sys.maxsize
for i in range(n):
    total = 0
    distance = 1
    for j in range(i+1, i+n):
        j %= n
        total += arr[j] * distance
        distance += 1
    
    min_move = min(total, min_move)
print(min_move)