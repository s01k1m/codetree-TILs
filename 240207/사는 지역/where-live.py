class Person:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region
people = []

for _ in range(int(input())):
    a, b, c = input().split()
    people.append(Person(a, b, c))

people = sorted(people, key=lambda x : x.name)

print(f"name {people[-1].name}")
print(f"addr {people[-1].address}")
print(f"city {people[-1].region}")