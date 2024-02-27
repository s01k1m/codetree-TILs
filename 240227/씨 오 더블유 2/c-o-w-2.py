n = int(input())
arr = list(str(input()))
l = len(arr)
ans = 0

for i in range(l):
    for j in range(i+1, l):
        for k in range(j+1, l):
            if arr[i] == "C" and arr[j] == "O" and arr[k] =="W":
                ans += 1
print(ans)