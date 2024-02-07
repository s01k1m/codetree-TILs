n = int(input())
circles = []

for i in range(n):
    n = i + 1
    a, b = map(int, input().split())
    circles.append((a, b, n))

circles.sort(key = lambda x: abs(x[1])+abs(x[0]))

for i in circles:
    print(i[2])