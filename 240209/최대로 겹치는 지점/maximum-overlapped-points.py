n = int(input())
arr = [0] * 100

for _ in range(n):
    a, b = map(int, input().split())
   # print(a,b)
    for i in range(a, b+1):
        arr[i-1] += 1

print(max(arr))