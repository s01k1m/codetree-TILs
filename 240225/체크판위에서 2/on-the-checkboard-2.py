r, c = map(int, input().split())
arr = [
    list(input().split())
    for _ in range(r)
]


ans = 0 
color = 0
for k in range(1, r-2):
    for v in range(1, c-2):
        if arr[k][v] != arr[0][0]:
            for a in range(k+1, r-1):
                for b in range(v+1, c-1):
                    if arr[0][0] == arr[a][b] and arr[k][v] == arr[r-1][c-1] :
                        ans += 1
                        # print( arr[0][0], arr[k][v],arr[a][b],arr[r-1][c-1])
                        # print(0,0,k,v, a,b,r-1,c-1)
print(ans)