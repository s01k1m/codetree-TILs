n = int(input())
arr = [0] * n
arr[0], arr[1] = map(int, input().split())

for i in range(2, n):
    sum = arr[i-1] + arr[i-2]
    new_sum = list(str(sum))

    arr[i] = int(new_sum[-1])

for _ in arr:
    print(_, end=" ")