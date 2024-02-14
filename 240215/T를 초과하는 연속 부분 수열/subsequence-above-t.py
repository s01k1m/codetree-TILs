n, t = map(int, input().split())
arr = list(map(int, input().split()))

mx, ans = 0, 0
for i in range(n):
    if i == 0 and arr[i] > t:
        ans += 1
    elif arr[i-1] > t and arr[i] > t:
        ans += 1
    else:
        ans = 1
    
    if mx < ans:
        mx = ans

print(mx)