n = int(input())
arr = list(map(int, input().split()))

class Sequence:
    def __init__(self, index, num, place=0):
        self.index, self.num, self.place = index, num , place

s = []
for idx, x in enumerate(arr):
    s.append(Sequence(idx, x))

s.sort(key = lambda x: x.num)

r = 0
for i in s:
    i.palce = r + 1
    r += 1

s.sort(key = lambda x: x.index)

for _ in range(n):
    print(s[_].palce, end= " ")