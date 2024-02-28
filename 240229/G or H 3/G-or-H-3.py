N, K = map(int,input().split())
arr = [
    0
    for _ in range(10001)
]

for _ in range(N):
    a, b = input().split()
    a = int(a)
    if b == "G":
        arr[a] = 1
    else:
        arr[a] = 2
ans = 0

for i in range(1, 10001+1-K):
    s = sum(arr[i:i+K+1])
    ans = max(ans,s)

print(ans)