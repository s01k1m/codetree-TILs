n = int(input())
arr = ["G" for _ in range(200001)]

cur = 100000

for _ in range(n):
    s, d = tuple(input().split())
    s = int(s)

    if d == "L":
        while s > 0:
            arr[cur] = "W"
            s -= 1
            if s > 0:
                cur -= 1
    elif d == "R":
        while s > 0:
            arr[cur] = "B"
            s -= 1
            if s > 0 :
                cur += 1
    
print(arr.count("W"), arr.count("B"))