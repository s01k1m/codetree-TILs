n = int(input())
ex = 0
cnt = 0
mx = 0

for _ in range(n):
    cur = int(input())

    if ex < cur:
        cnt += 1
    else:
        cnt = 1
    if mx < cnt:
        mx = cnt
    
    ex = cur
print(mx)