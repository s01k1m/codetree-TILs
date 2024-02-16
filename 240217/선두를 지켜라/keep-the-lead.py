M, N = map(int, input().split())

arr_A = []

for i in range(M):
    v, t = map(int, input().split())

    for _ in range(t):
        if len(arr_A) > 0:
            before = arr_A[-1]
        else:
            before = 0

        arr_A.append(before + v)

arr_B = []
for i in range(N):
    v, t = map(int, input().split())


    for _ in range(t):
        if len(arr_B) > 0:
            before = arr_B[-1]
        elif len(arr_B) == 0:
            before = 0
        arr_B.append(before + v)

first = []

for i in range(len(arr_A)):
    if arr_A[i] > arr_B[i]:
        first.append("A")
    elif arr_A[i] == arr_B[i]:
        first.append("AB")
    else:
        first.append("B")

ans = 0 
for i in range(1, len(first)):
    if first[i] != "AB" and first[i-1] != first[i]:
        ans += 1
print(ans)