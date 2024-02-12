n = int(input())
arr= [[0]*201 for _ in range(201)]


def square(a, b):
    for x in range(a, (a-8), -1):
        for y in range(b, (b-8), -1):
            arr[x][y] = 1


for _ in range(n):
    a, b = map(int, input().split())
    square(a+100, b+100)

ans = 0
for _ in(arr):
    ans += sum(_)

print(ans)