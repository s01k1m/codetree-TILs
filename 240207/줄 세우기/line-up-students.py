class Student:
    def __init__(self, num, height, weight, rate=0):
        self.num = num
        self.rate = rate
        self.height = height
        self.weight = weight

n = int(input())
students = []
for _ in range(n):
    a = _ + 1
    b, c = map(int, input().split())
    students.append(Student(a, b, c))

# 규칙 정렬
students.sort(key= lambda x: (-x.height, -x.weight, x.num))

# 등수
for _ in range(n):
    students[_].rate = _ + 1

# # 원래 순서대로 정렬
# students.sort(key= lambda x: x.rate)

for _ in(students):
    print(f"{_.height} {_.weight} {_.num}")