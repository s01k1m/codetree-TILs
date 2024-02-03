n, m =map(int, input().split())

x = int(min(n, m)**(1/2))

greatestCommoDivision = 0
for i in range(1, x+1):
    if n % i == 0 and m % i == 0:
        greatestCommoDivision = i
        # print(i)
    
if n == m :
    greatestCommoDivision = n
    
print(greatestCommoDivision)