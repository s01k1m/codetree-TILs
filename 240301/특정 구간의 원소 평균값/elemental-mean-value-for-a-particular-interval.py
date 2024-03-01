n = int(input())
arr = list(map(int, input().split()))

visited = [
    0
    for _ in range(n)
]

ans = 0
for i in range(n):
    for j in range(i, n):
        s = 0 
        for k in range(i, j+1):
            s += arr[k]
            visited[k] = 1

        avg = s/(j-i+1)
        for k in range(i, j+1):
            if avg == arr[k]:
                ans +=1
                break
                
            # if visited[v] == 0 and arr[v] == avg:
        
 
print(ans)