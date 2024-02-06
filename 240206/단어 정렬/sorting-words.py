n = int(input())
arr = [0] * n


for _ in range(n):
    arr[_] = input()


arr.sort()

for _ in range(n):
    print(arr[_])