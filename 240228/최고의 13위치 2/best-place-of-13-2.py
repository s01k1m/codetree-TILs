N = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

ans = []
def in_range(x,y):
    return 0 <= x, y, y+1, y+2 < N 

for i in range(N):
    for j in range(N-2):
        for k in range(N):
            for v in range(N-2):
                if i == k and j <= v <= j+2:
                    continue
                elif in_range(i,j) and in_range(k, v): 
                    s = (arr[i][j] + arr[i][j+1] + arr[i][j+2])+ (arr[k][v]+arr[k][v+1] + arr[k][v+2])
                    ans.append(s)

ans.sort(reverse=True)

print(ans[0])