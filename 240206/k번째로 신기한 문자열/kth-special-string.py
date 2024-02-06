n, k, T = input().split()
n = int(n)
k = int(k)
arr = [0]*n

for i in range(n):
    arr[i] = input()

arr.sort()

x = 0
l = len(T)

for i in range(n):

    str = arr[i]

    if str[:l] == T:
        x += 1
        if x == k:
            print(arr[i])
            break