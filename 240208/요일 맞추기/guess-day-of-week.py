m1, d1, m2, d2 = map(int, input().split())

days_of_month = [0, 31, 30, 31, 30, 31, 30, 31, 31, 30 ,31, 30, 31 ]
days = ['Mon', "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
elapsed_days = 0



if (m1 == m2 and d1 > d2) or (m1 > m2): # 기준일 달인데 그 전날
    while True:
        if m1 == m2 and d1 == d2:
            break
        
        d1 -= 1
        elapsed_days += 1

        if d1 < 1:
            m1 -= 1
            d1 = 1

elif m1 <= m2: # 기준일 같거나 그후
    while True:
        if m1 == m2 and d1 == d2:
            break
        
        d1 += 1
        elapsed_days += 1

        if d1 > days_of_month[m1]:
            m1 += 1
            d1 = 1


print(days[elapsed_days%7])