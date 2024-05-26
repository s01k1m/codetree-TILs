ans = 100
n = int(input())
arr = list(input())

jungbok_arr = [False] * n


# for i in range(n+1):
#     for j in range(i, n + 1):
#         if i == j:
#             continue
#         temp1 = arr[i: j]
#         flag = False
#         l = j-i

#         for x in range(0, n+1-l):
#             # print(i)
#             temp2 = arr[x:x+l]
#             if x != i and (temp1 == temp2):
#                 flag = True
#                 break

#         if flag != True:
#             print(temp1, temp2, l)
#             print()

# print(l)

for i in range(1, n): # 문자열 길이
    for j in range(0, n-i+1): # 그 문자열이 시작하는 인덱스
        temp_ans = i # i 는 길이
        # 길이 i인 문자열 중에 중복되는 것이 없으면 작은 i 일수록 답
        temp_arr = arr[j: j+i]

        if jungbok_arr[i]:
            continue

        for start in range(0, n-i+1):
            if j != start:
                compare_arr = arr[start: start+i]
                if compare_arr == temp_arr:
                    jungbok_arr[i] = True
                    break

for i in range(1, n+1):
    if jungbok_arr[i] == False:
        print(i)
        break