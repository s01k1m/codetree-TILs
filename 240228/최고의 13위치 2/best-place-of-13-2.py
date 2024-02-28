N = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

ans = []

for i in range(N):
    for j in range(N-2):
        s = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        ans.append(s)

ans.sort(reverse=True)

print(ans[0]+ ans[1])