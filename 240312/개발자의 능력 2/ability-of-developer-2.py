arr = list(map(int, input().split()))
l = len(arr)

ans = max(arr)
for i in range(1, l):
    for j in range(i+1, l):
        for m in range(1, l):
            for k in range(m+1, l):

                if i == m or j == k or j == m or i==k:
                    continue
                group1 = arr[i]+arr[j]
                group2 = arr[m]+arr[k]
                group3 = sum(arr) - group1 - group2
            
                diff = max(group1, group2, group3) - min(group1, group2, group3)
                ans = min(ans, diff)

print(ans)