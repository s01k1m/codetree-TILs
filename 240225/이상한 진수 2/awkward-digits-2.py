arr = list(map(int,str(input())))
new_arr = []

for i in range(len(arr)):
    if arr[i] == 0:
        new = arr[::]
        new[i] = 1
    else:
        new = arr[::]
        new[i] = 0

    new_arr.append(new)

ans = []

for l in new_arr:
    n = 0
    for i in l:
        n = 2 * n + i
    ans.append(n)

print(max(ans))