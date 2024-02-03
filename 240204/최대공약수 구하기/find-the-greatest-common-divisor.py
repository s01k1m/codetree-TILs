n, m =map(int, input().split())



def gcd(a, b):
    if a % b == 0:
        return b
    else:
        # print(b, a%b)
        return gcd(b, a%b)

greatestCommonDivision = gcd(n,m)
gcd(n,m)

print(greatestCommonDivision)