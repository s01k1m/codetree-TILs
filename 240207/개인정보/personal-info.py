people = []

for i in range(5):
    name, height, weight = input().split()
    people.append((name, int(height), float(weight)))

people.sort(key = lambda x: x[0])

print("name")
for p in people:
    print(p[0], p[1], p[2])

print()
print("height")
people.sort(key = lambda x: -x[1])

for p in people:
    print(p[0], p[1], p[2])