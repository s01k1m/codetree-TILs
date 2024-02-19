n, t= map(int,input().split())
arr =[
    [0] * n
    for _ in range(n)
]

directs = {
    'U':0,
    'D':3,
    'R':1,
    'L':2,
}
dx, dy = [-1, 0, 0, 1],[0, 1, -1, 0]

a, b, d = input().split()

a = int(a)
b = int(b)

def in_range(x, y):
    return 0 <= x <= n-1 and 0 <= y <=n-1

cur_x = a-1
cur_y = b-1
cur_d = directs[d]

while t > 0:    
    n_x = cur_x + dx[cur_d]
    n_y = cur_y + dy[cur_d]

    if in_range(n_x, n_y):
        t -= 1
        cur_x = n_x
        cur_y = n_y

    else:
        cur_d -= 3
        cur_d %= 4

            
        t -= 1
print(cur_x+1, cur_y+1)