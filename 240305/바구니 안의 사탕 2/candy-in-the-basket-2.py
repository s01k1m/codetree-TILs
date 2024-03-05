n, k = map(int, input().split())
arr = [0] * 101

for _ in range(n):
    a, b = map(int, input().split())
    arr[b] += a

def in_range(x):
    if 0<=x<=100:
        return arr[x]
    else:
        return False

max_candy = 0

for i in range(0,101):
    s = 0
    for j in range(i-k, i+k+1):
        if in_range(j):
            s += in_range(j)
    max_candy = max(s, max_candy)

    if max_candy == s:
        ans = i
print(max_candy)