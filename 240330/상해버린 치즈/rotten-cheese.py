# 사람수(P), 치즈 수(C) , 치즈 먹은 기록수(D), 아픈 기록수(S)
# 몇번째 사람(nth_p), 몇번째 치즈(nth_cheese), 언제 먹었는지(eat_time)  * 반복 D개
# 몇번째 사람(nth_p), 언제 확실히 아팠는지 * S개 반복

# ans: 약이 최대 몇 개나 필요한지를 출력합니다. -> 경우의 수가 여러개 라는 건가? no. 완벽하게 기록된 것이 아니기 때문에, 아프다고 기록되어 있는 사람 외의 다른 사람도 아플 수 있습니다. 

# 상한 치즈를 먹으면 1초가 지나야 아프다.
# 3 4 7 2
# ----먹은 기록
# 1 1 1
# 1 4 1
# 1 3 4
# 1 2 2
# 3 1 3 
# 2 1 5
# 2 2 7
'''

1번째 사람이 2초에 먹은 치즈는? 2번째 치즈임
2번째 사람이 7초에 먹은 치즈는? 2번째 치즈임
2번째 치즈를 먹은 사람은 총 몇명?


# ----
# 1 3
# 2 8

1번 사람이 3초 아팠다 / 2번 사람이 8초에 아팠다.
   1번 사람이 2초에 치즈를 먹었다
   2번 사람이 7초에 치즈를 먹었다
   
~내가 예상하는 로직 키핵심-> 치즈 순서대로 아픈 상황이 가능한 경우의수를 센다```
'''

# 클래스 선언
class Info1:
    def __init__(self, p, m, t):
        self.p, self.m, self.t = p, m, t

class Info2:
    def __init__(self, p, t):
        self.p, self.t = p, t

# 변수 선언 및 입력
n, m, d, s = tuple(map(int, input().split()))

info1 = []
for _ in range(d):
    p, x, t = tuple(map(int, input().split()))
    info1.append(Info1(p, x, t))

info2 = []
for _ in range(s):
    p, t = tuple(map(int, input().split()))
    info2.append(Info2(p, t))

ans = 0
    
# 하나의 치즈가 상했을 때 필요한 약의 수의 최댓값을 구합니다.
for i in range(1, m + 1):
    # i번째 치즈가 상했을 때 필요한 약의 수를 구합니다.

    # 우선 i번째 치즈가 상했다고 가정할 때 모순이 발생하지 않는지 확인합니다.
    # time배열을 만들어 각 사람이 언제 치즈를 먹었는지 저장합니다.
    time = [0] * (n + 1)
    for info in info1:
        # i번째 치즈에 대한 정보가 아닌 경우 넘어갑니다.
        if info.m != i:
            continue

        # person이 i번째 치즈를 처음 먹었거나
        # 이전보다 더 빨리 먹게 된 경우 time배열을 갱신합니다.
        person = info.p
        if time[person] == 0:
            time[person] = info.t
        elif time[person] > info.t:
            time[person] = info.t

    # possible : i번째 치즈가 상했을 수 있으면 true, 아니면 false
    possible = True

    for info in info2:
        # person이 i번째 치즈를 먹지 않았거나
        # i번째 치즈를 먹은 시간보다 먼저 아픈 경우 모순이 생깁니다.
        person = info.p
        if time[person] == 0:
            possible = False
        if time[person] >= info.t:
            possible = False

    # 만약 i번째 치즈가 상했을 가능성이 있다면, 몇 개의 약이 필요한지 확인합니다.
    pill = 0
    if possible:
        # 한번이라도 i번째 치즈를 먹은 적이 있다면, 약이 필요합니다.
        for j in range(1, n + 1):
            if time[j] != 0:
                pill += 1

    ans = max(ans, pill);

# 출력
print(ans)