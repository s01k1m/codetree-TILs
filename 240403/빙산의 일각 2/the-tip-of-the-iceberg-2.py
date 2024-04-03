n = int(input()) 
# 빙산 높이 array
arr = [
    int(input())
    for _ in range(n)
]

height = 0
max_height = max(arr)
ans = 0

for i in range(max_height+1):
    height = i
    iceberg = 0
    for i in range(n):
        if i == 0 and arr[i] > height:
            iceberg += 1
        elif i > 0 and arr[i] > height and arr[i-1] <= height:
            iceberg += 1
    if iceberg > ans:
        ans = iceberg 
print(ans)