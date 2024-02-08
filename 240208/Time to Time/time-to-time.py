a, b, c, d = map(int, input().split())
elapsedTime = 0

while True:
    if a == c and b == d:
        break
    
    elapsedTime += 1
    b += 1

    if b == 60:
        b = 0
        a += 1
    
print(elapsedTime)