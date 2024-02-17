max = 50000
arr_A = [0] * (max+1)
arr_B = [0] * (max+1)
a, b = map(int, input().split())

n = 1
for i in range(a):
    step, direction = input().split()
    step = int(step)
    if direction == "R":
        for j in range(step):
            arr_A[n] = arr_A[n-1] + 1
            n += 1
    elif direction == "L":
        for j in range(step):
            arr_A[n] = arr_A[n-1] - 1
            n += 1

for i in range(b):
    step, direction = input().split()
    step = int(step)
    if direction == "R":
        for j in range(step):
            arr_B[n] = arr_B[n-1] + 1
            n += 1
    elif direction == "L":
        for j in range(step):
            arr_B[n] = arr_B[n-1] - 1
            n += 1
ans = 0
for i in range(1, 50001):
    if (arr_A[i] != arr_A[i-1] or arr_B[i] != arr_B[i-1]) and arr_A[i] == arr_B[i]:
        ans += 1

print(ans)