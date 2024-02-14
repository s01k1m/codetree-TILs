n = int(input())

ex_sign = True # plus - > True minus => False
mx = 0
cnt = 0
for _ in range(n):
    cur = int(input())

    if cur > 0:
        cur_sign = True
    elif cur < 0:
        cur_sign = False


    if _ == 0 or cur_sign == ex_sign:
        cnt += 1
    else:
        cnt =1

    ex_sign = cur_sign

    if mx < cnt:
        mx = cnt

print(mx)