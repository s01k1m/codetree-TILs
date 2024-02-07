class Score:
    def __init__(self,name, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.name = name

n = int(input())
students = []

for i in range(n):
    a, b, c, d = input().split()

    students.append(Score(a, int(b), int(c), int(d)))

students.sort(key=lambda x: x.a + x.b + x.c)

for i in range(n):
    print(students[i].name, students[i].a,students[i].b,students[i].c)