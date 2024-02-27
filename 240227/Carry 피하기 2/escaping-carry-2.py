n = int(input())

arr = [
    input()
    for _ in range(n)
]
ans = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a = int(arr[i])
            b = int(arr[j])
            c = int(arr[k])

            flag = True
            t = 10000
                        
            while t >= 1:

                s = a // t + b // t + c // t
                a = a % t
                b = b % t
                c = c % t

                if s >= 10:
                    flag = False
                    break

                t /= 10
            
            if flag:
                ans.append(int(arr[i])+int(arr[j])+int(arr[k]))

if ans:
    print(max(ans))
else:
    print(-1)