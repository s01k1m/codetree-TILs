digit_2_list = list(input())
n = 0

for i in digit_2_list:
    n = (n * 2) + int(i)


n *= 17

digit_2_list = []

while True:
    if n < 2:
         digit_2_list.append(n)
         break

    digit_2_list.append(n % 2)
    n = n // 2

for i in digit_2_list[::-1]:
    print(i , end= "")