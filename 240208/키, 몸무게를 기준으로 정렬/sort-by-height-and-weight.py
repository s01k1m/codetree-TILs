n = int(input())
student = []
for _ in range(n):
    a, b, c = input().split()
    student.append((a, int(b), int(c)))

student.sort(key = lambda x: (x[1],-x[2]))

for i in student:
    print(i[0], i[1], i[2])