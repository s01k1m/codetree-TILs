n, k = map(int, input().split())
answer = []

def print_anwer():
    for e in answer:
        print(e, end=" ")
    print()

def choose(curr):
    if curr == n + 1: # 종료조건
        print_anwer()
        return
    for i in range(1, k+1):
        answer.append(i)
        choose(curr+1)
        answer.pop()

    return

choose(1)