a, b, c = map(int, input().split())
x = y = z = 11
elapsed_min = 0

if a < 11 and b < 11 and c < 11:
    print(-1)
else:

    while True:
        if x == a and y == b and z == c:
            break
        z += 1
        elapsed_min += 1

        if z == 60:
            z = 0
            y += 1

        if y == 24:
            y = 0
            x += 1

print(elapsed_min)