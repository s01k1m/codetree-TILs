class Score:
    def __init__(self,name, kr, eng, math):
        self.name = name
        self.kr = kr
        self.eng = eng
        self.math = math

n = int(input())
students = []

for _ in range(n):
    a, b, c, d = input().split()
    students.append(Score(a, int(b), int(c), int(d) ))

students.sort(key = lambda x: (-x.kr, -x.eng, -x.math))

for _ in range(n):
    print(students[_].name , students[_].kr,students[_].eng, students[_].math)