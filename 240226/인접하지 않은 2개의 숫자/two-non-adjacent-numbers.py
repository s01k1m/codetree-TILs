n = int(input())
arr = list(map(int, input().split()))
max_s = 0
for i in range(n-2):
    for j in range(i+1, n):
        s = arr[i] + arr[j]
        max_s = max(max_s,s)

print(max_s)