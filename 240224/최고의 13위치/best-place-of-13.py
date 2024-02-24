n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c = 1, 3
max_cnt = 0
for i in range(0, n):
    for j in range(0, n-c+1):
        
        if max_cnt <= (arr[i][j]+ arr[i][j+1] + arr[i][j+2]):
            max_cnt = (arr[i][j]+ arr[i][j+1] + arr[i][j+2])

print(max_cnt)