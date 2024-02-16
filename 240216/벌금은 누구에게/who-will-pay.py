N, M, K = map(int, input().split())
arr = [0] * (N+1)

answer = 0 

for _ in range(M):
    a = int(input())
    arr[a] += 1
    if arr[a] == K:
        answer = a
        break

if answer:
    print(answer)
else:
    print(-1)