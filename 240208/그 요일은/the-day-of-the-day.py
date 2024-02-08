m1, d1, m2, d2 = map(int, input().split())
a = input()

days_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
elapsed_days = 0

while True:
    if m1 == m2 and d1 == d2:
        break
    
    elapsed_days += 1
    d1 += 1
    
    if d1 > days_of_month[m1]:
        d1 = 1
        m1 += 1

remainder = elapsed_days % 7
share = elapsed_days // 7

if remainder >= ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun").index(a):
    share += 1

print(share)