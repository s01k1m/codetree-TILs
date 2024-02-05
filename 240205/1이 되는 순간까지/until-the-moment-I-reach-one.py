def f(n, cnt):
    if n == 1:
        return print(cnt)
    if n % 2 == 0: # 짝수라면
        return f(n/2, cnt+1)
    else : # 홀수라면
        return f(n//3, cnt+1)

n = int(input())

f(n,0)