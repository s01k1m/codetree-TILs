n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = 1000 * 1000 * 2
for i in range(n):
    for j in range(i+1, n ):
        temp = (arr[i][0]- arr[j][0])**2 + (arr[i][1]- arr[j][1])**2
        ans = min(temp,ans)
print(ans)