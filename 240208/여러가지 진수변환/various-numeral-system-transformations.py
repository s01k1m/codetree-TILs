N, B = map(int, input().split())
digit = []

while N >= 4:
    digit.append(N % 4)
    N = N // 4

if N < 4:
    digit.append(N)
for i in digit[::-1]:
    print(i, end="")