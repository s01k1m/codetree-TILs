a, b = map(int, input().split())
n =input()

n = list(map(int, list(n)))

origin_n = 0

for i in n:
    origin_n = origin_n * a + i

n_based_B = []

while True:
    if origin_n < b:
        n_based_B.append(origin_n)
        break

    n_based_B.append(origin_n % b)
    origin_n = origin_n // b

for i in n_based_B:
    print(i, end="")