maxD = 1000 * 1000
arr_A = [0]* (maxD+1)
arr_B = [0]* (maxD+1)

a, b = map(int,input().split())

n = 1
for i in range(a):
    v, t = map(int, input().split())
    for i in range(t):
        arr_A[n] = arr_A[n-1] + v
        n += 1

n = 1
for i in range(b):
    v, t = map(int, input().split())
    for i in range(t):
        arr_B[n] = arr_B[n-1] + v
        n += 1

arr = [0] * (n)

for i in range(0, n):
    if arr_A[i] == arr_B[i]:
        arr[i] = "AB"
    
    elif arr_A[i] > arr_B[i]:
        arr[i] = "A"
    else:
        arr[i] = "B"

ans = 0 
for i in range(1, n):
    if arr[i] != arr[i-1]:
        ans +=1
print(ans)