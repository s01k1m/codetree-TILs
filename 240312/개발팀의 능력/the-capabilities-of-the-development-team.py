arr=list( map(int, input().split()))
n = len(arr)
ans = max(arr)
for i in range(n):
    for j in range(i+1, n):
        for k in range(n):
            if i == k or j == k:
                continue
            group1 = arr[i] + arr[j]
            group2 = arr[k]
            group3 = sum(arr) - group1 - group2
            if group1 == group2 or group2 == group3 or group1 == group3:
                continue
            diff = max(group1, group2, group3) - min(group1, group2, group3)
            ans = min(diff, ans)
if ans == max(arr):
    print(-1)
else:
    print(ans)