N, S = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0

diff = S
for i in range(N):
    for j in range(i+1, N):
        s = 0
        for x in range(N):
            if x == i or x== j:
                continue
            s += arr[x]
        if abs(S-s) <= diff:
            ans = abs(S-s)
            diff = abs(S-s)

print(ans)