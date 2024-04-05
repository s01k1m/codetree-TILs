import sys

N = int(input())
arr = list(map(int,input().split()))

ans = sys.maxsize
for idx in range(N): # 2배를 할 숫자 arr[idx]
    arr[idx] *= 2
    for dlt in range(N):
        if idx == dlt:
            pass
        sum = 0
        for i in range(1, N):
            if i == dlt:
                pass
            if i == dlt+1 and i > 1:
                sum += abs(arr[i-2] - arr[i])
            elif i == dlt+1 and i== 1:
                pass
            else:
                sum += abs(arr[i-1] - arr[i]) 

        ans = min(sum, ans)



    arr[idx] = arr[idx] // 2 # 원상 복구

print(ans)