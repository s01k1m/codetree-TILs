arr = list(str(input()))
l = len(arr)

ans = 0
for i in range(l-1):
    
    if arr[i] =="(" and arr[i+1] =="(":
        # )) 찾기 시작
        for j in range(i+2, l-1):
            if arr[j] == ")" and arr[j+1] == ")":
                ans += 1
print(ans)