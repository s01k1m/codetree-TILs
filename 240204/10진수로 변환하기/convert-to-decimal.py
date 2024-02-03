binary = list(map(int, input().split()))
num = 0

for i in range(5):
    num = num * 2 + binary[i-1]

print(num)