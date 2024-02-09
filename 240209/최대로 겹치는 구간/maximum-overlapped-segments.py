n = int(input())
arr = [0] * 200
for _ in range(n):
    a, b = map(int, input().split())
    a += 100
    b += 100

    for i in range(a, b):
        arr[i-1] += 1
    
max = 0
for i in range(200):
    if arr[i] > max:
        max = arr[i]

print(max)