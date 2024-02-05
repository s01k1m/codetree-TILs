n = int(input())
arr = list(map(int, input().split()))

def max_v(a):
    if a == 0:
        return arr[0]

    return max(max_v(a-1), arr[a])

print(max_v(n-1))