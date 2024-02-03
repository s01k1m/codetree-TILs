binary = list(map(int, list(input())))
# print(binary)
num = 0
# print(len(binary))
for i in range(len(binary)):
    num = num * 2 + binary[i]

print(num)