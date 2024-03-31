# 
global c
global g
global h

n, c, g, h = map(int, input().split()) # 작업량
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def cal(t, ta, tb):
    if t < ta:
        return c
    elif ta <= t <= tb:
        return g
    elif tb < t:
        return h

min_t = 0
max_t = 1000
ans = 0

for temperature in range(min_t, max_t+1):
    s = 0
    for idx in range(n):
       s += cal(temperature, arr[idx][0], arr[idx][1])
    ans = max(ans, s)

print(ans)