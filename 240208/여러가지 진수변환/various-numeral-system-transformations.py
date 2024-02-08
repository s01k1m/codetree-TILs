N, B = map(int, input().split())
digit = []

while N >= B:
    digit.append(N % B)
    N = N // B

if N < B:
    digit.append(N)
for i in digit[::-1]:
    print(i, end="")