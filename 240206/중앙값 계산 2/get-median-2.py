def median(arr):
    arr.sort()

    n = len(arr) // 2

    print(arr[n], end=" ")

n = int(input())
original = list(map(int, input().split()))

arr = []

for i in range(n):
    arr.append(original[i])

    if (i+1) % 2:
        median(arr)