n = int(input())
arr = list(map(int, input().split()))


def f(n, big, arr):
    if n >= len(arr):
        return big
    if arr[n] > big:
        big = arr[n]
    
    return f(n+1, big, arr)
    

print(f(0, arr[0], arr))