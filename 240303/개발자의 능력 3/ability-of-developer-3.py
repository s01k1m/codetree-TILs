arr = list(map(int, input().split()))

n = len(arr)


maxx = 6000000
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i != k :
                s = arr[i]+ arr[j] + arr[k]
                maxx = min(abs(sum(arr)-2*s), maxx)
print(maxx)