N = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

cnt = 0 

# B가 말한 세 자리 수에 있는 숫자들 중 하나가 A가 생각한 세 자리 수의 동일한 자리에 위치한다면 1번 카운트가 하나 올라갑니다.
def strike(ans, guess):
    strike = 0
    for ii in range(3):
        if int(ans[ii]) != int(guess[ii]):
            # print(int(ans[ii]),int(guess[ii]))
            continue
        strike += 1
    return strike

# B가 말한 세 자리 수에 있는 숫자들 중 하나가 A가 생각한 세 자리 수에 있긴 하나 다른 자리에 위치하면 2번 카운트가 하나 올라갑니다.

def ball(ans, guess):
    b = 0
    if ans[0] == guess[1] or ans[0] == guess[2]:
        b +=1
    if ans[1] == guess[0] or ans[1] == guess[2]:
        b +=1
    if ans[2] == guess[0] or ans[2] == guess[1]:
        b +=1

    return b
# 이때, ball은 숫자만 같아야하기 때문에 즉, 자릿수는 달라야하기 때문에 숫자와 자릿수가 모두 같은 strike를 빼줍니다!
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if (i == j or j== k or i == k):
                continue

            n = [i,j,k]
            flag = True

            for x in range(N):
                ans = n
                # ans: 답 후보
                guess = arr[x][0] 
                # 예측 숫자
                guess = list(map(int, str(guess)))

                if int(arr[x][1]) == strike(n, guess):
                    pass
                else:
                    flag = False
                    continue
                if int(arr[x][2]) == ball(n, guess):
                    pass
                else:
                    flag = False
                    continue

            if flag:
                cnt += 1

print(cnt)