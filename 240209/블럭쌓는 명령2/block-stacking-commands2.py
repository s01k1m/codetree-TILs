N, K = map(int, input().split())

arr = [0] * (N+1)

for _ in range(K):
    s, e = map(int, input().split())

    for i in range(s, e+1):
        arr[i] += 1

print(max(arr))