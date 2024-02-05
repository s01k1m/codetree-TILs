def lcd(n):
    if n == 0:
        return arr[0]
    if n == 1:
        return arr[0] * arr[1] / gcd(arr[0], arr[1])
    return arr[n] * lcd(n-1) / gcd(lcd(n-1), arr[n])

n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(int(lcd(n-1)))