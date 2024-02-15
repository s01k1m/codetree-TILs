a, b = (map(int, input().split()))

arr_A = [0]
arr_B = [0]

for i in range(a):
    d, n = input().split()
    n = int(n)
    cur = arr_A[-1]
    if d == "R":
        for j in range(n):
            cur+=1
            arr_A.append(cur)
            
    else:
        for j in range(n):
            cur-=1
            arr_A.append(cur)

for i in range(b):
    d, n = input().split()
    n = int(n)
    cur = arr_B[-1]
    if d == "R":
        for j in range(n):
            cur+=1
            arr_B.append(cur)
    else:
        for j in range(n):
            cur-=1
            arr_B.append(cur)

answer = 0 
for i in range(1, len(arr_A)):

    if arr_A[i] == arr_B[i]:
        answer = i
        break
        
if answer:
    print(answer)
else:
    print(-1)