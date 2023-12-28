n = int(input())

for i in range(1, n+1):
    for j in range(0, n):
        print(i *(2**j), end=" ")
    print()