n = int(input())
arr = list(map(int, input().split()))

ans = 0

for i in range(n):
    cnt = 1
    last = arr[i]
    for j in range(i+1, n):
        if last <= arr[j]:
            cnt += 1
            last = arr[j]
            for k in range(j+1, n):
                if last <= arr[k]:
                    cnt += 1
                    if cnt == 3:
                        ans += 1
                        cnt = 2
                        continue
                cnt = 2
        cnt = 1
        last = arr[i]
    cnt =1
print(ans)