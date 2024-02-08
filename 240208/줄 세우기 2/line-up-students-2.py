class St:
    def __init__(self, height, weight, n):
        self.height = height
        self.n = n
        self.weight = weight

n = int(input())
students = []

for i in range (n):
    i_height, i_weight = map(int, input().split()) 
    students.append(St(int(i_height), int(i_weight), i + 1))

students.sort(key= lambda x : (x.height, -x.weight))

for i in (students):
    print(i.height, i.weight, i.n)