n = int(input())
cnt = 1
ex = 1001
mx = 0
x = 0
for _ in range(n):
    x = int(input())
    if  ex == x:
        cnt += 1
    else:
        cnt = 1
    if mx < cnt:
        mx = cnt 
    ex = x
print(mx)